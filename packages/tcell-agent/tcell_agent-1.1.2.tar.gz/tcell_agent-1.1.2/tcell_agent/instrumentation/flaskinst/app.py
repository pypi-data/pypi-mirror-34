# -*- coding: utf-8 -*-
# Copyright (C) 2015 tCell.io, Inc. - All Rights Reserved

from __future__ import unicode_literals

import sys


from tcell_agent.agent import TCellAgent, PolicyTypes
from tcell_agent.appsensor.manager import app_sensor_manager
from tcell_agent.appsensor.meta import AppSensorMeta
from tcell_agent.instrumentation import safe_wrap_function
from tcell_agent.instrumentation.flaskinst.database import check_database_errors
from tcell_agent.instrumentation.flaskinst.headers import flask_add_headers, check_location_redirect
from tcell_agent.instrumentation.flaskinst.js_agent import insert_js_agent
from tcell_agent.instrumentation.flaskinst.meta import create_meta, \
    update_meta_with_response, set_context_and_start_timer
from tcell_agent.request_metrics.timing import end_timer
from tcell_agent.tcell_logger import get_module_logger


def check_patches_blocking(request):
    request._ip_blocking_triggered = False

    rust_policies = TCellAgent.get_policy(PolicyTypes.RUST)
    if rust_policies and rust_policies.patches_enabled and \
       rust_policies.block_request(request._appsensor_meta):
        request._ip_blocking_triggered = True
        from flask.wrappers import Response
        return Response('', 403)

    return None


def run_appsensor_check(request, response, response_code):
    rust_policies = TCellAgent.get_policy(PolicyTypes.RUST)
    if rust_policies and rust_policies.appfirewall_enabled and not request._ip_blocking_triggered:
        appsensor_meta = request._appsensor_meta
        update_meta_with_response(appsensor_meta, response, response_code)
        app_sensor_manager.send_appsensor_data(appsensor_meta)


def set_tcell_vars(request):
    request._appsensor_meta = AppSensorMeta()
    request._ip_blocking_triggered = False


def start_agent():
    get_module_logger(__name__).info("Starting agent")
    TCellAgent.get_agent().ensure_polling_thread_running()

    from tcell_agent.instrumentation.flaskinst.routes import report_routes
    safe_wrap_function("Report Routes", report_routes)


def _instrument():
    from tcell_agent.instrumentation.flaskinst.routes import instrument_routes
    safe_wrap_function("Instrument Routes", instrument_routes)

    from flask.globals import _request_ctx_stack

    tcell_func = Flask.__init__

    def init(self, *args, **kwargs):
        result = tcell_func(self, *args, **kwargs)

        self.before_first_request_funcs.append(start_agent)

        return result

    Flask.__init__ = init

    tcell_preprocess_request = Flask.preprocess_request

    def preprocess_request(self):
        safe_wrap_function("Start Request Timer", set_context_and_start_timer, _request_ctx_stack.top.request)
        # run this to ensure variables required by process_response are set
        # before calling original method because original method might raise an exception
        safe_wrap_function("Set TCell Vars", set_tcell_vars, _request_ctx_stack.top.request)

        result = tcell_preprocess_request(self)

        safe_wrap_function("Set Meta on Request", create_meta, _request_ctx_stack.top.request)
        block_ip_response = safe_wrap_function(
            "Checking for block rules",
            check_patches_blocking,
            _request_ctx_stack.top.request)
        if block_ip_response:
            return block_ip_response

        return result

    Flask.preprocess_request = preprocess_request

    tcell_process_response = Flask.process_response

    def process_response(self, response):
        result = tcell_process_response(self, response)

        from flask.wrappers import Response
        if isinstance(response, Response):
            safe_wrap_function(
                "AppFirewall Request/Response",
                run_appsensor_check,
                _request_ctx_stack.top.request,
                result,
                result.status_code)
            result = safe_wrap_function(
                "Insert Body Tag",
                insert_js_agent,
                _request_ctx_stack.top.request,
                result)
            safe_wrap_function(
                "Add Headers",
                flask_add_headers,
                _request_ctx_stack.top.request,
                result)
            safe_wrap_function(
                "Check Location Header",
                check_location_redirect,
                _request_ctx_stack.top.request,
                result)

        safe_wrap_function("Stop Request Timer", end_timer, _request_ctx_stack.top.request)

        return result

    Flask.process_response = process_response

    tcell_handle_user_exception = Flask.handle_user_exception

    def handle_user_exception(self, user_exception):
        try:
            safe_wrap_function("Set Meta after exception happened", create_meta, _request_ctx_stack.top.request)
            exc_type, exc_value, stack_trace = sys.exc_info()
            safe_wrap_function(
                "Check for database errors",
                check_database_errors,
                _request_ctx_stack.top.request,
                exc_type,
                stack_trace)
            return tcell_handle_user_exception(self, user_exception)
        except Exception:
            safe_wrap_function("Stop Request Timer", end_timer, _request_ctx_stack.top.request)
            safe_wrap_function(
                "AppFirewall Request/Response",
                run_appsensor_check,
                _request_ctx_stack.top.request,
                None,
                500)

            from flask._compat import reraise
            exc_type, exc_value, stack_trace = sys.exc_info()
            reraise(exc_type, exc_value, stack_trace)

    Flask.handle_user_exception = handle_user_exception


try:
    from flask import Flask

    if TCellAgent.get_agent():
        _instrument()
except ImportError:
    pass
except Exception as exception:
    get_module_logger(__name__).debug("Could not instrument flask: {e}".format(e=exception))
    get_module_logger(__name__).debug(exception, exc_info=True)
