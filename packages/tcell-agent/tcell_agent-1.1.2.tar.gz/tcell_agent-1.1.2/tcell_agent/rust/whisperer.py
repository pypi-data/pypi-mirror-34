import sys
import json
import os

from ctypes import cdll, c_uint8, c_void_p, c_size_t, c_int, c_char_p, POINTER

from tcell_agent.config.configuration import CONFIGURATION
from tcell_agent.rust.request_response import create_request_response, create_patches_request
from tcell_agent.tcell_logger import get_module_logger
from tcell_agent.utils.compat import to_bytes


def get_linux_variant():
    if ("linux" in sys.platform) and os.path.isfile("/etc/alpine-release"):
        return "alpine-"

    return ""


version = "1.3.0"
prefix = {"win32": ""}.get(sys.platform, "lib")
extension = {"darwin": ".dylib", "win32": ".dll"}.get(sys.platform, ".so")
variant = get_linux_variant()


try:
    library_filename = "{}tcellagent-{}{}{}".format(prefix, variant, version, extension)
    native_lib = cdll.LoadLibrary(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               library_filename)))

    ###
    # All calls below have the following response interface
    #
    #    restype [int]: 0+ length of buffer_out answer
    #                   -1 general error
    #                   -2 buffer_out is null
    #                   -X buffer_out is not big enough for response. X represents how big the response was going to be
    ###

    native_lib.create_agent.argtypes = [c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.create_agent.restype = c_int

    native_lib.update_policies.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.update_policies.restype = c_int

    native_lib.appfirewall_apply.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.appfirewall_apply.restype = c_int

    native_lib.patches_apply.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.patches_apply.restype = c_int

    native_lib.cmdi_apply.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.cmdi_apply.restype = c_int

    native_lib.get_headers.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.get_headers.restype = c_int

    native_lib.get_js_agent_script_tag.argtypes = [c_void_p, c_char_p, c_size_t, POINTER(c_uint8), c_size_t]
    native_lib.get_js_agent_script_tag.restype = c_int

    native_lib.free_agent.argtypes = [c_void_p]
    native_lib.free_agent.restype = c_int

except Exception as ex:
    native_lib = None

    get_module_logger(__name__).error("Failed to load common agent library. {e}".format(e=ex))
    get_module_logger(__name__).debug(ex, exc_info=True)


def get_library_response(function_called, response, response_len):
    if response_len < 0:
        get_module_logger(__name__).warn(
            "Error response from `{}` in native library: {}".format(function_called,
                                                                    response_len))
    else:
        try:
            result = json.loads("".join([chr(response_byte)
                                         for response_byte in response[:response_len]]))
            if result.get('error'):
                get_module_logger(__name__).error(
                    "{} returned an error: {}".format(function_called, result["error"])
                )
                result = {}

            return result
        except ValueError:
            get_module_logger(__name__).warn("Could not decode json response from" +
                                             "`{}` in native library.".format(function_called))

    return {}


def create_agent():
    if native_lib:
        agent_config = {
            "skip_logger": True,
            "application": {
                "app_id": CONFIGURATION.app_id,
                "api_key":  CONFIGURATION.api_key,
                "allow_payloads": CONFIGURATION.allow_payloads,
                "js_agent_api_base_url": CONFIGURATION.js_agent_api_base_url,
                "js_agent_url": CONFIGURATION.js_agent_url
            },
            "appfirewall": {
                "enable_body_xxe_inspection": False,
                "enable_body_json_inspection": False,
                "allow_log_payloads": True
            },
            "policy_versions": {
                "patches": 1,
                "login": 1,
                "appsensor": 2,
                "regex": 1,
                "csp-headers": 1,
                "http-redirect": 1,
                "clickjacking": 1,
                "secure-headers": 1,
                "canaries": 1,
                "dlp": 1,
                "cmdi": 1,
                "jsagentinjection": 1
            },
            "max_header_size": CONFIGURATION.max_csp_header_bytes or (1024 * 1024)
        }
        config_bytes = to_bytes(json.dumps(agent_config))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.create_agent(
            config_bytes, len(config_bytes), response, allocated_memory_bytes
        )
        return get_library_response("create_agent", response, response_len)

    return {}


def free_agent(agent_ptr):
    if native_lib:
        native_lib.free_agent(agent_ptr)


def update_policies(agent_ptr, policy):
    if native_lib and policy:
        policy_bytes = to_bytes(json.dumps(policy))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.update_policies(
            agent_ptr, policy_bytes, len(policy_bytes), response, allocated_memory_bytes
        )
        return get_library_response("update_policies", response, response_len)

    return {}


def apply_appfirewall(agent_ptr, appsensor_meta):
    if native_lib and agent_ptr and appsensor_meta:
        request_response = create_request_response(appsensor_meta=appsensor_meta)
        request_response_bytes = to_bytes(json.dumps(request_response))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.appfirewall_apply(agent_ptr,
                                                    request_response_bytes,
                                                    len(request_response_bytes),
                                                    response,
                                                    allocated_memory_bytes)

        return get_library_response("apply_appfirewall", response, response_len)

    return {}


def apply_patches(agent_ptr, appsensor_meta):
    if native_lib and agent_ptr and appsensor_meta:
        patches_request = create_patches_request(appsensor_meta=appsensor_meta)
        patches_request_bytes = to_bytes(json.dumps(patches_request))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.patches_apply(agent_ptr,
                                                patches_request_bytes,
                                                len(patches_request_bytes),
                                                response,
                                                allocated_memory_bytes)

        return get_library_response("apply_patches", response, response_len)

    return {}


def apply_cmdi(agent_ptr, cmd, tcell_context):
    if native_lib and agent_ptr and cmd and cmd.strip():
        command_info = {
            "command": cmd,
            "method": tcell_context and tcell_context.method,
            "path": tcell_context and tcell_context.path
        }
        command_bytes = to_bytes(json.dumps(command_info))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.cmdi_apply(agent_ptr,
                                             command_bytes,
                                             len(command_bytes),
                                             response,
                                             allocated_memory_bytes)

        return get_library_response("apply_cmdi", response, response_len)

    return {}


def get_headers(agent_ptr, tcell_context):
    if native_lib and agent_ptr and tcell_context:
        headers_request = {
            "method": tcell_context.method,
            "path": tcell_context.path,
            "route_id": tcell_context.route_id,
            "session_id": tcell_context.session_id
        }
        headers_request_bytes = to_bytes(json.dumps(headers_request))

        allocated_memory_bytes = 1024 * 16
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.get_headers(agent_ptr,
                                              headers_request_bytes,
                                              len(headers_request_bytes),
                                              response,
                                              allocated_memory_bytes)
        return get_library_response("get_headers", response, response_len)

    return {}


def get_js_agent_script_tag(agent_ptr, tcell_context):
    if native_lib and agent_ptr and tcell_context:
        js_agent_req = {
            "method": tcell_context.method,
            "path": tcell_context.path
        }
        js_agent_req_bytes = to_bytes(json.dumps(js_agent_req))

        allocated_memory_bytes = 1024 * 8
        buf_type = c_uint8 * allocated_memory_bytes
        response = buf_type()  # allocate memory
        response_len = native_lib.get_js_agent_script_tag(agent_ptr,
                                                          js_agent_req_bytes,
                                                          len(js_agent_req_bytes),
                                                          response,
                                                          allocated_memory_bytes)

        return get_library_response("get_js_agent_script_tag", response, response_len)

    return {}
