# Copyright (C) 2015 tCell.io, Inc. - All Rights Reserved

from __future__ import unicode_literals

from tcell_agent.config.configuration import CONFIGURATION
from tcell_agent.sanitize.sanitize_utils import SanitizeUtils
from tcell_agent.sanitize.passwords import fingerprint_password
from tcell_agent.sensor_events.base_event import SensorEvent


class LoginEvent(SensorEvent):
    def __init__(self):
        super(LoginEvent, self).__init__("login")
        self.raw_referrer = None
        self.raw_uri = None

    def success(self, *args, **kwargs):
        self["event_name"] = "login-success"
        return self._add_details(*args, **kwargs)

    def failure(self, *args, **kwargs):
        self["event_name"] = "login-failure"
        return self._add_details(*args, **kwargs)

    def _add_details(self,
                     user_id,
                     user_agent,
                     referrer,
                     remote_address,
                     header_keys,
                     document_uri,
                     session_id=None,
                     user_valid=None,
                     password=None):
        self.raw_referrer = referrer
        self.raw_uri = document_uri

        if user_agent:
            self["user_agent"] = user_agent
        if remote_address:
            self["remote_addr"] = remote_address
        if header_keys:
            self["header_keys"] = header_keys

        if session_id:
            self["session"] = session_id

        fingerprinted_password = fingerprint_password(password, user_id)
        if fingerprinted_password:
            self["password_id"] = fingerprinted_password

        if user_id is not None:
            if CONFIGURATION.hipaa_safe_mode:
                self["user_id"] = SanitizeUtils.hmac(str(user_id))
            else:
                self["user_id"] = str(user_id)

        if user_valid is not None:
            self["user_valid"] = user_valid

        return self

    def post_process(self):
        if self.raw_uri is not None:
            self["document_uri"] = SanitizeUtils.strip_uri(self.raw_uri)

        if self.raw_referrer is not None:
            if CONFIGURATION.hipaa_safe_mode:
                self["referrer"] = SanitizeUtils.hmac(SanitizeUtils.strip_uri(self.raw_referrer))
            else:
                self["referrer"] = SanitizeUtils.strip_uri(self.raw_referrer)
