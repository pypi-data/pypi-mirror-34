# encoding=utf-8
import unittest

from mock import Mock, patch


from tcell_agent.appsensor.meta import AppSensorMeta
from tcell_agent.config.configuration import CONFIGURATION
from tcell_agent.instrumentation.context import TCellInstrumentationContext
from tcell_agent.rust.whisperer import create_agent, free_agent, update_policies, \
     apply_appfirewall, apply_patches, apply_cmdi, get_library_response, \
     get_js_agent_script_tag
from tcell_agent.utils.compat import to_bytes


class WhispererTest(unittest.TestCase):
    def setUp(self):
        self.old_app_id = CONFIGURATION.app_id
        self.old_api_key = CONFIGURATION.api_key
        self.old_js_agent_api_base_url = CONFIGURATION.js_agent_api_base_url
        self.old_js_agent_url = CONFIGURATION.js_agent_url
        self.old_max_csp_header_bytes = CONFIGURATION.max_csp_header_bytes

        CONFIGURATION.app_id = "app_id"
        CONFIGURATION.api_key = "api_key"
        CONFIGURATION.js_agent_api_base_url = "js_agent_api_base_url"
        CONFIGURATION.js_agent_url = "js_agent_url"

    def tearDown(self):
        CONFIGURATION.app_id = self.old_app_id
        CONFIGURATION.api_key = self.old_api_key
        CONFIGURATION.js_agent_api_base_url = self.old_js_agent_api_base_url
        CONFIGURATION.js_agent_url = self.old_js_agent_url
        CONFIGURATION.max_csp_header_bytes = self.old_max_csp_header_bytes

    def js_agent_test(self):
        whisper = create_agent()
        self.assertIsNotNone(whisper.get("agent_ptr"))
        agent_ptr = whisper.get("agent_ptr")

        policy = {
            "jsagentinjection": {
                "state": "Enabled",
                "enabled": True,
                "api_key": "js_agent_api_key",
                "excludes": [],
                "policy_id": "jsagentinjection-v1-1",
                "version": 1
            }
        }
        whisper = update_policies(agent_ptr, policy)

        tcell_context = TCellInstrumentationContext()
        tcell_context.method = "GET"
        tcell_context.path = "/"
        script_tag_info = get_js_agent_script_tag(agent_ptr, tcell_context)
        expected_script_tag = '<script src="{}" tcellappid="{}" tcellapikey="{}" tcellbaseurl="{}"></script>'.format(
            "js_agent_url",
            "app_id",
            "js_agent_api_key",
            "js_agent_api_base_url"
        )

        self.assertEqual(
            script_tag_info,
            {"script_tag": expected_script_tag}
        )

        free_agent(agent_ptr)

    def empty_command_apply_cmdi_test(self):
        whisper = create_agent()
        self.assertIsNotNone(whisper.get("agent_ptr"))
        agent_ptr = whisper["agent_ptr"]

        policy = {
            "cmdi": {
                "data": {
                    "collect_full_commandline": False,
                    "command_rules": [
                        {
                            "action": "report",
                            "rule_id": "TJM4ODvkB2jSR47qltL+0Nyy/PGlF6Qa/cin65qtIlc="
                        }
                    ],
                    "compound_statement_rules": [
                        {
                            "action": "report",
                            "rule_id": "Y+IHN7BJDctqOIIZOb71NR8PkUxru01LDkqU1lZwogY="
                        }
                    ]
                },
                "policy_id": "0cf0f090-ffc0-11e7-8080-808080808080",
                "version": 1
            }
        }
        whisper = update_policies(agent_ptr, policy)
        self.assertEqual(whisper.get("enablements"),
                         {
                             "appfirewall": False,
                             "patches": False,
                             "cmdi": True,
                             "headers": False,
                             "jsagentinjection": False
                         })

        commands = apply_cmdi(agent_ptr, "sh -c \"bundle install && bundle exec rake db:setup\"", None)
        self.assertEqual(commands,
                         {'apply_response': {'full_commandline': None,
                                             'matches': [{'command': None,
                                                          'rule_id': 'Y+IHN7BJDctqOIIZOb71NR8PkUxru01LDkqU1lZwogY='},
                                                         {'command': 'sh',
                                                          'rule_id': 'TJM4ODvkB2jSR47qltL+0Nyy/PGlF6Qa/cin65qtIlc='},
                                                         {'command': 'bundle',
                                                          'rule_id': 'TJM4ODvkB2jSR47qltL+0Nyy/PGlF6Qa/cin65qtIlc='},
                                                         {'command': 'bundle',
                                                          'rule_id': 'TJM4ODvkB2jSR47qltL+0Nyy/PGlF6Qa/cin65qtIlc='}],
                                             'blocked': False,
                                             'commands': [{'command': 'sh',
                                                           'arg_count': 2},
                                                          {'command': 'bundle',
                                                           'arg_count': 1},
                                                          {'command': 'bundle',
                                                           'arg_count': 3}]}})

        free_agent(agent_ptr)

    def create_agent_test(self):
        whisper = create_agent()
        self.assertIsNotNone(whisper.get("agent_ptr"))
        agent_ptr = whisper["agent_ptr"]

        policy = {
            "regex": {
                "data": {
                    "patterns": [
                        {
                            "id": "tc-xss-1",
                            "pattern": "(?:<(script|iframe|embed|frame|frameset|object|img|applet|body|html|style|layer|link|ilayer|meta|bgsound))",
                            "sensor": "xss",
                            "title": "Basic Injection"
                        }
                    ],
                    "version": 1518546622571
                },
                "policy_id": "f3a313b0-10eb-11e8-8080-808080808080",
                "version": 1
            },

            "appsensor": {
                "policy_id": "f39d6e60-10eb-11e8-8080-808080808080",
                "version": 2,
                "data": {
                    "sensors": {
                        "ignore_rules": [],
                        "errors": {
                            "csrf_exception_enabled": True,
                            "sql_exception_enabled": True
                        },
                        "xss": {
                            "dynamic_patterns": ["tc-xss-1"],
                            "patterns": ["1"]
                        }
                    }
                }
            },

            "patches": {
                "data": {
                    "block_rules": [],
                    "blocked_ips": [],
                    "payloads": {
                        "send_payloads": True,
                    },
                    "rules": [
                        {
                            "action": "BlockIf",
                            "destinations": {"check_equals": [{"path": "*"}]},
                            "id": "check-present-rule",
                            "ignore": [],
                            "matches": [{
                                "all": [{
                                    "parameters": {
                                        "check_present": {
                                            "queries": [
                                                "xss_param"
                                            ]
                                        }
                                    }
                                }],
                                "any": []
                            }],
                            "title": "check present rule"
                        }
                    ]
                },
                "policy_id": "patches-v1-14",
                "version": 2
            },

            "cmdi": {
                "data": {
                    "collect_full_commandline": False,
                    "command_rules": [
                        {
                            "action": "report",
                            "rule_id": "TJM4ODvkB2jSR47qltL+0Nyy/PGlF6Qa/cin65qtIlc="
                        }
                    ],
                    "compound_statement_rules": [
                        {
                            "action": "report",
                            "rule_id": "Y+IHN7BJDctqOIIZOb71NR8PkUxru01LDkqU1lZwogY="
                        }
                    ]
                },
                "policy_id": "0cf0f090-ffc0-11e7-8080-808080808080",
                "version": 1
            }
        }

        whisper = update_policies(agent_ptr, policy)
        self.assertEqual(whisper.get("enablements"),
                         {
                             "appfirewall": True,
                             "cmdi": True,
                             "patches": True,
                             "headers": False,
                             "jsagentinjection": False
                         })

        appsensor_meta = AppSensorMeta()
        appsensor_meta.remote_address = "192.168.1.1"
        appsensor_meta.method = "GET"
        appsensor_meta.path = "/some/path"
        appsensor_meta.location = "http://192.168.1.1/some/path?xss_param=<script>"
        appsensor_meta.route_id = "12345"
        appsensor_meta.session_id = "session_id"
        appsensor_meta.user_id = "user_id"
        appsensor_meta.request_content_bytes_len = 1024
        appsensor_meta.response_content_bytes_len = 2048
        appsensor_meta.get_dict = {"xss_param": "<script>"}
        appsensor_meta.path_dict = {}
        appsensor_meta.post_dict = {}
        appsensor_meta.files_dict = {}
        appsensor_meta.json_body_str = "{}"
        appsensor_meta.cookie_dict = {}
        appsensor_meta.headers_dict = {}
        appsensor_meta.user_agent_str = "Mozilla"
        appsensor_meta.encoding = "utf-8"
        appsensor_meta.sql_exceptions = [{"exception_name": "OperationalError", "exception_payload": "Developer Error"}]
        appsensor_meta.csrf_reason = "invalid csrf token"

        whisper = apply_appfirewall(
            agent_ptr,
            appsensor_meta
        )

        self.assertEqual(whisper,
                         {"apply_response": [{"detection_point": "xss",
                                              "pattern": "tc-xss-1",
                                              "route_id": "12345",
                                              "remote_address": "192.168.1.1",
                                              "meta": {"num_headers": 0,
                                                       "h": [],
                                                       "l": "query",
                                                       "summary": []},
                                              "user_id": "user_id",
                                              "uri": "http://192.168.1.1/some/path?xss_param=",
                                              "parameter": "xss_param",
                                              "session_id": "session_id",
                                              "method": "GET"},
                                             {"detection_point": "exsql",
                                              "route_id": "12345",
                                              "remote_address": "192.168.1.1",
                                              "user_id": "user_id",
                                              "uri": "http://192.168.1.1/some/path?xss_param=",
                                              "parameter": "OperationalError",
                                              "session_id": "session_id",
                                              "method": "GET"},
                                             {"detection_point": "excsrf",
                                              "route_id": "12345",
                                              "remote_address": "192.168.1.1",
                                              "user_id": "user_id",
                                              "uri": "http://192.168.1.1/some/path?xss_param=",
                                              "session_id": "session_id",
                                              "method": "GET"}]})

        appsensor_meta = AppSensorMeta()
        appsensor_meta.method = "GET"
        appsensor_meta.path = "/some/path"
        appsensor_meta.remote_address = "192.168.1.1"
        appsensor_meta.request_content_bytes_len = 1024
        appsensor_meta.get_dict = {"xss_param": "<script>"}
        appsensor_meta.post_dict = {}
        appsensor_meta.files_dict = {}
        appsensor_meta.json_body_str = "{}"
        appsensor_meta.cookie_dict = {}
        appsensor_meta.headers_dict = {}
        appsensor_meta.encoding = "utf-8"

        whisper = apply_patches(agent_ptr=agent_ptr, appsensor_meta=appsensor_meta)
        self.assertEqual(whisper,
                         {"apply_response": {"patches_policy_id": "patches-v1-14",
                                             "payload": [{"l": "query", "name": "xss_param", "val": "<script>"}],
                                             "regex_pid": "f3a313b0-10eb-11e8-8080-808080808080",
                                             "status": "Blocked",
                                             "rule_id": "check-present-rule"}})

        free_agent(agent_ptr)

    def error_response_get_library_response_test(self):
        mock_logger = Mock()
        with patch("tcell_agent.rust.whisperer.get_module_logger", return_value=mock_logger):
            whisper = get_library_response("create_agent", to_bytes(""), -1)
            self.assertTrue(mock_logger.warn.called)
            mock_logger.warn.assert_called_once_with(
                'Error response from `create_agent` in native library: -1')
            self.assertEqual(whisper, {})

    def json_decode_error_get_library_response_test(self):
        mock_logger = Mock()
        with patch("tcell_agent.rust.whisperer.get_module_logger", return_value=mock_logger):
            response = [ord(c) for c in list("malformed_json}")]
            response_len = len(response)
            whisper = get_library_response("create_agent", response, response_len)
            self.assertTrue(mock_logger.warn.called)
            mock_logger.warn.assert_called_once_with(
                'Could not decode json response from`create_agent` in native library.')
            self.assertEqual(whisper, {})

    def valid_get_library_response_test(self):
        mock_logger = Mock()
        with patch("tcell_agent.rust.whisperer.get_module_logger", return_value=mock_logger):
            response = [ord(c) for c in list('{"success":true}')]
            response_len = len(response)
            whisper = get_library_response("create_agent", response, response_len)
            self.assertFalse(mock_logger.warn.called)
            self.assertEqual(whisper, {"success": True})
