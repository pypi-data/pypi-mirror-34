# -*- coding: utf-8 -*-
# Copyright (C) 2015 tCell.io, Inc. - All Rights Reserved

""" Agent Module handles communication and instrumentation, this
is the main class.
"""

from __future__ import unicode_literals
from __future__ import print_function


import threading
import time
import json
from queue import Queue, Empty, Full
import os
import tcell_agent
import traceback
import random

from tcell_agent.config.configuration import CONFIGURATION

from tcell_agent.api import TCellAPI, TCellAPIException
from tcell_agent.policies.http_redirect_policy import HttpRedirectPolicy
from tcell_agent.policies.dataloss_policy import DataLossPolicy
from tcell_agent.policies.login_policy import LoginPolicy
from tcell_agent.policies.honeytoken_policy import HoneytokenPolicy
from tcell_agent.policies.rust_policies import RustPolicies

from tcell_agent.sensor_events.server_agent_packages import ServerAgentPackagesEvent
from tcell_agent.sensor_events.server_agent_details import ServerAgentDetailsEvent
from tcell_agent.sensor_events.metrics import MetricsEvent
from tcell_agent.sensor_events.discovery import DiscoveryEvent
from tcell_agent.sensor_events.app_route import AppRouteSensorEvent
from tcell_agent.sensor_events.flush_dummy import FlushDummyEvent
from tcell_agent.sensor_events.app_config_settings import AppConfigSettings

from tcell_agent.routes.route_discovery import RouteTable

from tcell_agent import system_info
from tcell_agent.policy_cache import TCellPolicyCache

from .fork_manager import ForkPipeManager
from .metrics import AgentMetrics

from tcell_agent.tcell_logger import get_module_logger

lock = threading.Lock()
agentLock = threading.Lock()
pollingLock = threading.Lock()
forkThreadsLock = threading.Lock()
eventHandlerThreadsLock = threading.Lock()


class TCellAgentSettingEvent(AppConfigSettings):
    def __init__(self, name, value):
        super(TCellAgentSettingEvent, self).__init__("tcell", "config", name=name, value=value)


class PolicyTypes(object):
    CSP = "csp-headers"
    SECURE_HEADERS = "secure-headers"
    HTTP_TX = "http-tx"
    HTTP_REDIRECT = "http-redirect"
    CLICKJACKING = "clickjacking"
    DATALOSS = DataLossPolicy.api_identifier
    APPSENSOR = RustPolicies.appfirewall_identifier
    LOGIN = LoginPolicy.api_identifier
    HONEYTOKEN = HoneytokenPolicy.api_identifier
    PATCHES = RustPolicies.patches_identifier
    COMMAND_INJECTION = RustPolicies.cmdi_identifier
    RUST = RustPolicies.api_identifier
    REGEX = RustPolicies.regex_identifier
    JS_AGENT = RustPolicies.jsagent_identifier


class TCellAgent(object):
    """Agent Class for holding and managing threads."""
    policy_classes = {
        PolicyTypes.HTTP_REDIRECT: HttpRedirectPolicy,
        PolicyTypes.DATALOSS: DataLossPolicy,
        PolicyTypes.LOGIN: LoginPolicy,
        PolicyTypes.HONEYTOKEN: HoneytokenPolicy}
    tCell_agent = None

    def __init__(self):
        LOGGER = get_module_logger(__name__)
        """Initialize policies and threads"""
        LOGGER.info("Initializing agent")
        try:
            self.parent_pid = os.getpid()
        except Exception as ex:
            LOGGER.exception("Exception getting operating system pid: {0}".format(type(ex)))
            raise

        self.policies = {}
        try:
            policy_types = list(TCellAgent.policy_classes)
            for policy_type in policy_types:
                self.policies[policy_type] = TCellAgent.policy_classes[policy_type]()

        except Exception:
            LOGGER.exception("Exception loading policy types.")
            raise
        self.policies[PolicyTypes.RUST] = RustPolicies()

        self.shutdown = False

        LOGGER.info("Initializing IO Pipe")

        def event_callback(value):
            try:
                TCellAgent.send(value)
            except Exception as ex:
                LOGGER.debug("Exceptions handling event callback")
                LOGGER.debug(ex)

        self.fork_pipe_manager = ForkPipeManager(event_callback)
        self.fork_pipe_queue = Queue(100)
        self.fork_pipe_thread = None
        self.fork_pipe_broken = False  # If the forked event send fails, start up an event manager

        def metrics_callback(value):
            try:
                _metric = value.get("_metric", None)
                LOGGER.debug("Handling callback for {metric}".format(metric=_metric))
                if _metric == "request_metric":
                    TCellAgent.request_metric(
                        value.get("route_id"),
                        value.get("request_time"),
                        value.get("ip"),
                        value.get("user_agent"),
                        value.get("session_id"),
                        value.get("user_id")
                    )
                elif _metric == "discover_database_fields":
                    TCellAgent.discover_database_fields(
                        value.get("database"),
                        value.get("schema"),
                        value.get("table"),
                        value.get("fields"),
                        value.get("route_id")
                    )
                elif _metric == "discover_route":
                    TCellAgent.discover_route(
                        value.get("route_url"),
                        value.get("route_method"),
                        value.get("route_target"),
                        value.get("route_id")
                    )
                else:
                    LOGGER.debug("Unknown metric type through pipe")
                    LOGGER.debug(_metric)
            except Exception as ex:
                LOGGER.debug("Exceptions handling metrics callback")
                LOGGER.debug(ex)

        self.metrics_pipe_manger = ForkPipeManager(metrics_callback)
        self.metrics_pipe_queue = Queue(100)
        self.metrics_pipe_thread = None

        self.polling_thread = None
        self.polling_thread_pid = os.getpid()

        self.event_handling_thread = None
        LOGGER.info("Checking cache")

        self.policy_cache = TCellPolicyCache(CONFIGURATION.app_id, CONFIGURATION.cache_folder)

        LOGGER.info("Checking preload policy file")
        try:
            if CONFIGURATION.preload_policy_filename:
                self.load_policy_from_file(CONFIGURATION.preload_policy_filename)
            self.process_policies(self.policy_cache.current_cache(), cache=False)
        except Exception:
            LOGGER.exception("Exception reading cache policy filename")
            raise

        LOGGER.info("Initializing route table.")
        self.route_table = RouteTable()

        self.event_queue = Queue(CONFIGURATION.event_queue_intake_size)
        self.events_to_dispatch = []
        self.agent_metrics = AgentMetrics()

    def in_fork(self):
        return self.parent_pid != os.getpid()

    def ensure_polling_thread_running(self):
        if self.is_polling_thread_running():
            return
        pollingLock.acquire()
        try:
            if self.is_polling_thread_running():
                return
            self.start_polling_thread()
        finally:
            pollingLock.release()

    def is_polling_thread_running(self):
        return self.polling_thread and self.polling_thread.isAlive() and self.polling_thread_pid == os.getpid()

    def start_polling_thread(self):
        """Start the background threads for polling/events"""
        self.polling_thread = threading.Thread(target=self.run_polling, args=())
        self.polling_thread.daemon = True  # Daemonize thread
        self.polling_thread.start()  # Start the execution
        self.polling_thread_pid = os.getpid()
        get_module_logger(__name__).info("Starting the policy-polling thread")

    def ensure_metrics_pipe_thread_running(self):
        if self.is_metrics_pipe_thread_running():
            return
        forkThreadsLock.acquire()
        try:
            if self.is_metrics_pipe_thread_running():
                return
            self.start_metrics_pipe_thread()
        finally:
            forkThreadsLock.release()

    def is_metrics_pipe_thread_running(self):
        return self.metrics_pipe_thread and self.metrics_pipe_thread.isAlive()

    def start_metrics_pipe_thread(self):
        def run_metrics_fork_thread():
            while True:
                value = self.metrics_pipe_queue.get(True)
                get_module_logger(__name__).debug("Fork metrics thread received metric")
                sent_successfully = self.metrics_pipe_manger.send_to_parent(value)
                if not sent_successfully:
                    self.fork_pipe_broken = True

        get_module_logger(__name__).debug("Starting metrics pipe thread")
        self.metrics_pipe_thread = threading.Thread(target=run_metrics_fork_thread, args=())
        self.metrics_pipe_thread.daemon = True  # Daemonize thread
        self.metrics_pipe_thread.start()

    def ensure_fork_pipe_thread_running(self):
        if self.is_fork_pipe_thread_running():
            return
        forkThreadsLock.acquire()
        try:
            if self.is_fork_pipe_thread_running():
                return
            self.start_fork_pipe_thread()
        finally:
            forkThreadsLock.release()

    def is_fork_pipe_thread_running(self):
        return self.fork_pipe_thread and self.fork_pipe_thread.isAlive()

    def start_fork_pipe_thread(self):
        def run_event_fork_thread():
            while True:
                event = self.fork_pipe_queue.get(True)
                get_module_logger(__name__).debug("Fork event thread received event")
                sent_successfully = self.fork_pipe_manager.send_to_parent(event)
                if not sent_successfully:
                    self.fork_pipe_broken = True

        get_module_logger(__name__).debug("Starting event pipe thread")
        self.fork_pipe_thread = threading.Thread(target=run_event_fork_thread, args=())
        self.fork_pipe_thread.daemon = True  # Daemonize thread
        self.fork_pipe_thread.start()

    def ensure_event_handler_thread_running(self):
        if self.in_fork() and not self.fork_pipe_broken:
            self.ensure_fork_pipe_thread_running()
            self.ensure_metrics_pipe_thread_running()
            return
        if self.is_event_handler_thread_running():
            return
        eventHandlerThreadsLock.acquire()
        try:
            if self.is_event_handler_thread_running():
                return
            self.start_event_handler()
        finally:
            eventHandlerThreadsLock.release()

    def is_event_handler_thread_running(self):
        return self.event_handling_thread and self.event_handling_thread.isAlive()

    def start_event_handler(self):
        initial_events = [
            ServerAgentDetailsEvent(
                user=tcell_agent.system_info.current_username(),
                group=tcell_agent.system_info.current_group_id(),
                language='Python',
                language_version=system_info.python_version_string()),
            TCellAgentSettingEvent("logging_directory", CONFIGURATION.log_directory),
            TCellAgentSettingEvent("allow_payloads", CONFIGURATION.allow_payloads),
            TCellAgentSettingEvent("reverse_proxy", CONFIGURATION.reverse_proxy)
        ]
        if CONFIGURATION.logging_options:
            logging_enabled = CONFIGURATION.logging_options.get("enabled", True)
            if logging_enabled:
                initial_events.append(TCellAgentSettingEvent("logging_enabled", "true"))
                initial_events.append(
                    TCellAgentSettingEvent("logging_level", CONFIGURATION.logging_options.get("level", "INFO")))

                # Deprecated: this is so we can ensure no one is using this setting so we can remove
                # the code altogether in the future
                if CONFIGURATION.logging_options.get("log_dir", None):
                    initial_events.append(
                        TCellAgentSettingEvent("deprecated_log_dir",
                                               CONFIGURATION.logging_options.get("log_dir")))
            else:
                initial_events.append(TCellAgentSettingEvent("logging_enabled", "false"))
        if CONFIGURATION.hmac_key is not None:
            initial_events.append(TCellAgentSettingEvent("hmac_key_present", "true"))
        else:
            initial_events.append(TCellAgentSettingEvent("hmac_key_present", "false"))
        if CONFIGURATION.reverse_proxy:
            initial_events.append(TCellAgentSettingEvent("reverse_proxy_ip_address_header",
                                                         CONFIGURATION.reverse_proxy_ip_address_header))
        if CONFIGURATION.config_filename is not None:
            initial_events.append(TCellAgentSettingEvent("config_filename", CONFIGURATION.config_filename))

        from tcell_agent.rust.whisperer import native_lib
        initial_events.append(TCellAgentSettingEvent("native_lib_loaded", native_lib is not None))

        self.events_to_dispatch = initial_events
        self.flush_events()
        sape = ServerAgentPackagesEvent()

        def add_package_to_event(package_obj):
            sape.add_package(package_obj.key, package_obj.version)

        system_info.get_packages(add_package_to_event)
        self.events_to_dispatch = [sape]
        self.flush_events()

        self.event_handling_thread = threading.Thread(target=self.run_event_handler, args=())
        self.event_handling_thread.daemon = True  # Daemonize thread
        self.event_handling_thread.start()
        get_module_logger(__name__).info("Starting the event-manager thread")

    def load_policy_from_file(self, policy_filename):
        """Loads either preload policy file or cache file"""
        if not os.path.isfile(policy_filename):
            get_module_logger(__name__).error("Could not find the policy file: {policy_filename}".format(policy_filename=policy_filename))
            return
        with open(policy_filename) as data_file:
            policies_json = json.load(data_file)
            if policies_json.get("result"):
                policies_json = policies_json["result"]
            self.process_policies(policies_json, cache=False)

    def process_policies(self, policies_json, cache=True):
        """Given a piece of JSON (from API or file) process it"""
        LOGGER = get_module_logger(__name__)
        policy_types = list(TCellAgent.policy_classes)
        for policy_type in policy_types + [PolicyTypes.CSP,
                                           PolicyTypes.SECURE_HEADERS,
                                           PolicyTypes.CLICKJACKING,
                                           PolicyTypes.APPSENSOR,
                                           PolicyTypes.PATCHES,
                                           PolicyTypes.COMMAND_INJECTION,
                                           PolicyTypes.REGEX,
                                           PolicyTypes.JS_AGENT]:
            policy_json = policies_json.get(policy_type)
            if policy_json is not None:
                if cache:
                    self.policy_cache.update_cache(policy_type, policy_json)

                try:
                    if policy_type in TCellAgent.policy_classes:
                        self.policies[policy_type] = TCellAgent.policy_classes[policy_type](policy_json)
                except Exception as general_exception:
                    LOGGER.error("Exception parsing {policy_type} policy".format(
                        policy_type=policy_type))
                    LOGGER.exception(general_exception)

        try:
            self.policies[PolicyTypes.RUST].load_from_json(policies_json)
        except Exception as general_exception:
            LOGGER.error("Exception parsing {policy_type} policy".format(
                policy_type=PolicyTypes.RUST))
            LOGGER.exception(general_exception)

    def call_update(self, last_id):
        LOGGER = get_module_logger(__name__)
        # Make one update request from the tCell service
        if not CONFIGURATION.fetch_policies_from_tcell:
            self.shutdown = True
            return None

        if CONFIGURATION.version != 0 and CONFIGURATION.version != 1:
            raise TCellAPIException("Unsupported configuration version")

        try:
            result = TCellAPI.v1update(last_id)
            if self.shutdown:
                return last_id

            if result:
                last_id = result.get("last_id")
                self.process_policies(result)

            return last_id
        except TCellAPIException as tcell_api_exception:
            LOGGER.error("result exception, sleeping 30 seconds")
            LOGGER.debug(tcell_api_exception)
            time.sleep(30)
        except Exception as general_exception:
            LOGGER.error("result general exception, sleeping 120 seconds {e}".format(e=general_exception))
            LOGGER.debug(general_exception, exc_info=True)
            time.sleep(120)
        return last_id

    def run_polling(self):
        # Method that runs forever
        last_id = None
        while not self.shutdown:
            previous_timestamp = last_id
            last_id = self.call_update(last_id)
            if (previous_timestamp is None) and (not CONFIGURATION.demomode):
                # Just prevent two rapid requests at once.
                sleeptime = random.randint(5, 20)
                time.sleep(sleeptime)

    def addEvent(self, event):
        """Add an event to the queue to be sent to tcell"""
        if event is None:
            return
        get_module_logger(__name__).debug("Adding event {event} to queue".format(event=event.get_debug_data()))
        self.ensure_event_handler_thread_running()
        try:
            if event.queue_wait:
                self.event_queue.put(event, True, 10)
            else:
                self.event_queue.put_nowait(event)
        except Full:
            pass

    def add_event_to_fork(self, event):
        get_module_logger(__name__).debug("Adding event {event} to fork".format(event=event.get_debug_data()))
        self.ensure_fork_pipe_thread_running()
        try:
            self.fork_pipe_queue.put_nowait(event)
        except Full:
            pass

    def add_metric_to_fork(self, value):
        get_module_logger(__name__).debug("Adding metric {value} to fork".format(value=value))
        self.ensure_metrics_pipe_thread_running()
        try:
            self.metrics_pipe_queue.put_nowait(value)
        except Full:
            pass

    def _request_metric_counter(self, route_id, request_time):
        if route_id is None or route_id == "":
            route_id = "?"
        self.agent_metrics.add_route_count(route_id, request_time)
        if self.agent_metrics.should_send_flush_event_for_route_count_table():
            TCellAgent.send(FlushDummyEvent())

    def run_event_handler(self):
        # Prevent one event every 59 seconds from stopping events from being sent
        last_batch_time_diff = time.time()
        while not self.shutdown:
            try:
                time_limit = CONFIGURATION.event_time_limit_seconds
                time_since_send = time.time() - last_batch_time_diff
                time_diff = max(0, (time_limit - time_since_send))
                item = self.event_queue.get(True, time_diff)
                self.consume_event(item)
                self.event_queue.task_done()
                batch_limit = CONFIGURATION.event_batch_size_limit
                if item.flush_right_away:
                    last_batch_time_diff = time.time()
                    self.flush_events()
                elif len(self.events_to_dispatch) >= batch_limit:
                    last_batch_time_diff = time.time()
                    self.flush_events()
            except Empty:
                last_batch_time_diff = time.time()
                self.flush_events()
                continue

    def filter_all_ensure_events(self):
        keep_events = [event for event in self.events_to_dispatch if event.ensure_delivery]
        keep_events = keep_events[:200]
        self.events_to_dispatch = keep_events

    def flush_events(self):
        """Send queued events as a batch to the tCell service"""
        try:
            metrics_table = self.agent_metrics.get_and_reset_route_count_table()
            metrics_session = self.agent_metrics.get_and_reset_sesssion_metric()
            if metrics_table or metrics_session:
                metrics_event = MetricsEvent()
                if metrics_table:
                    metrics_event.set_rct(metrics_table)
                if metrics_session:
                    metrics_event.set_session(metrics_session)
                events = self.events_to_dispatch + [metrics_event]
            else:
                events = self.events_to_dispatch
            response_code = TCellAPI.v1send_events(events)
            if response_code == 200:
                self.events_to_dispatch = []
            else:
                self.filter_all_ensure_events()
        except Exception as connection_exception:
            LOGGER = get_module_logger(__name__)
            LOGGER.error("Error sending events, will try again later {e}".format(e=connection_exception))
            LOGGER.debug(connection_exception, exc_info=True)
            self.filter_all_ensure_events()

    def consume_event(self, event):
        """Event is added directly, not by queue"""
        event.post_process()
        if event.send_event:
            self.events_to_dispatch.append(event)

    # cmdi events are special because they can be triggered very easily by running any shell command
    # startup scripts are likely to run shell commands. it's not a good idea to startup the event
    # processor before worker processses are forked, so the safest thing to do is let a different
    # event start the event processor to avoid deadlocking worker processes.
    # more details: https://github.com/tcellio/pythonagent-tcell/pull/221
    @classmethod
    def is_it_safe_to_send_cmdi_events(cls):
        try:
            return cls.get_agent().in_fork() or cls.get_agent().is_event_handler_thread_running()
        except:
            return False

    @classmethod
    def send(cls, event):
        LOGGER = get_module_logger(__name__)
        try:
            cls.get_agent().ensure_event_handler_thread_running()
            if cls.get_agent().in_fork() and not cls.get_agent().fork_pipe_broken:
                LOGGER.debug("Sending event {event} by fork".format(event=event.get_debug_data()))
                cls.get_agent().add_event_to_fork(event)
            else:
                LOGGER.debug("Sending event {event} by queue".format(event=event.get_debug_data()))
                cls.get_agent().addEvent(event)
        except Exception as e:
            LOGGER.error("could not send event, no agent initialized {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)

    @classmethod
    def get_policy(cls, policy_type):
        try:
            return cls.get_agent().policies.get(policy_type)
        except Exception as e:
            LOGGER = get_module_logger(__name__)
            LOGGER.error("could not get policy, no agent initialized {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)

    @classmethod
    def get_agent(cls):
        if cls.tCell_agent is not None:
            return cls.tCell_agent
        else:
            LOGGER = get_module_logger(__name__)
            lock.acquire()
            try:
                if CONFIGURATION.app_id is None or CONFIGURATION.api_key is None:
                    LOGGER.error(
                        "Application ID and API Key must be set by configuration file or environmental variables.")
                    return None
                if cls.tCell_agent is not None:
                    return cls.tCell_agent
                cls.tCell_agent = TCellAgent()
            except Exception:
                LOGGER.exception("Exception creating agent.")
                traceback.print_exc()
                raise
            finally:
                lock.release()
            return cls.tCell_agent

    @classmethod
    def get_route_table(cls):
        try:
            return cls.get_agent().route_table
        except Exception as e:
            LOGGER = get_module_logger(__name__)
            LOGGER.error("could not get route_table, no agent initialized {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)

    @classmethod
    def request_metric(cls, route_id, request_time, ip, user_agent, session_id=None, user_id=None):
        LOGGER = get_module_logger(__name__)
        try:
            if cls.get_agent().in_fork() and not cls.get_agent().fork_pipe_broken:
                LOGGER.debug("Request metric sending (in fork) {route_id} {request_time}".format(route_id=route_id,
                                                                                                 request_time=request_time))
                cls.get_agent().add_metric_to_fork({
                    "_metric": "request_metric",
                    "route_id": route_id,
                    "ip": ip,
                    "user_agent": user_agent,
                    "request_time": request_time,
                    "session_id": session_id,
                    "user_id": user_id
                })
            else:
                try:
                    login_policy = cls.get_policy(PolicyTypes.LOGIN)
                    if login_policy and login_policy.session_hijacking_metrics and user_id:
                        cls.get_agent().agent_metrics.add_session_track_metric(session_id, user_id, user_agent, ip)
                        if cls.get_agent().agent_metrics.should_send_flush_event():
                            cls.send(FlushDummyEvent())
                except Exception as exceptionAddingLoginMetric:
                    LOGGER.error("Exception adding login metric {e}".format(e=exceptionAddingLoginMetric))
                    LOGGER.error(exceptionAddingLoginMetric)

                LOGGER.debug(
                    "Request metric sending %s %s",
                    route_id,
                    request_time)

                cls.get_agent()._request_metric_counter(route_id, request_time)
        except Exception as e:
            LOGGER.error("could not add metric {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)

    @classmethod
    def discover_route(cls, route_url, route_method, route_target, route_id):
        try:
            if cls.get_agent().in_fork() and not cls.get_agent().fork_pipe_broken:
                cls.get_agent().add_metric_to_fork({
                    "_metric": "discover_route",
                    "route_url": route_url,
                    "route_method": route_method,
                    "route_target": route_target,
                    "route_id": route_id})
                return
            if cls.get_agent() is not None:
                if not cls.get_route_table().routes[route_id].discovered:
                    TCellAgent.send(AppRouteSensorEvent(
                        route_url,
                        route_method,
                        route_target,
                        route_id
                    ))
                    cls.get_route_table().routes[route_id].discovered = True
        except Exception as e:
            LOGGER = get_module_logger(__name__)
            LOGGER.error("could not add route discovery {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)

    @classmethod
    def discover_database_fields(cls, database, schema, table, fields, route_id=None):
        try:
            if cls.get_agent().in_fork() and not cls.get_agent().fork_pipe_broken:
                cls.get_agent().add_metric_to_fork({
                    "_metric": "discover_database_fields",
                    "database": database,
                    "schema": schema,
                    "table": table,
                    "fields": fields,
                    "route_id": route_id})
                return

            if cls.tCell_agent is not None:
                dlp_policy = cls.get_policy(PolicyTypes.DATALOSS)
                if dlp_policy is None:
                    return
                if route_id is None:
                    route_id = ""

                if (cls.get_agent().route_table.routes[route_id].have_fields_been_discovered(database, schema, table,
                                                                                             fields)):
                    cls.get_agent().route_table.routes[route_id].set_fields_discovered(database, schema, table, fields)
                    event = DiscoveryEvent(route_id).for_database_fields(database, schema, table, fields)
                    cls.send(event)
                    cls.get_agent().route_table.update_cache_flag = True
            else:
                return
        except Exception as e:
            LOGGER = get_module_logger(__name__)
            LOGGER.error("could not add database discovery fields {e}".format(e=e))
            LOGGER.debug(e, exc_info=True)
