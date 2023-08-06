# -*- coding: utf-8 -*-
# Copyright (C) 2015 tCell.io, Inc. - All Rights Reserved

from __future__ import unicode_literals

from tcell_agent.agent import TCellAgent
from tcell_agent.tcell_logger import get_module_logger


_started = False
_route_table_sent = False
_dlp_success = False
_default_charset = 'utf-8'


def _instrument():
    from tcell_agent.instrumentation.djangoinst.middleware.csrf_exception_middleware import instrument_csrf_view_middleware
    from tcell_agent.instrumentation.djangoinst.database_error_wrapper import instrument_database_error_wrapper, \
        handle_django15_exception
    from django.core.handlers.base import BaseHandler

    old_load_middleware = BaseHandler.load_middleware

    def load_middleware(*args, **kwargs):
        get_module_logger(__name__).info("Adding middleware")
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.body_filter_middleware.BodyFilterMiddleware')
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.afterauthmiddleware.AfterAuthMiddleware')
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.tcelllastmiddleware.TCellLastMiddleware')
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.tcell_data_exposure_middleware.TCellDataExposureMiddleware',
            atIdx=0)
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.globalrequestmiddleware.GlobalRequestMiddleware',
            atIdx=0)
        _insertMiddleware(
            'tcell_agent.instrumentation.djangoinst.middleware.timermiddleware.TimerMiddleware')

        if _dlp_success:
            from tcell_agent.instrumentation.djangoinst.dlp import dlp_instrumentation  # noqa pylint: disable=redefined-outer-name
            dlp_instrumentation()

        if _is_csrf_middleware_enabled():
            instrument_csrf_view_middleware()

        instrument_database_error_wrapper()

        import tcell_agent.instrumentation.djangoinst.contrib_auth  #  noqa pylint: disable=unused-variable
        return old_load_middleware(*args, **kwargs)

    BaseHandler.load_middleware = load_middleware

    if hasattr(BaseHandler, "handle_uncaught_exception"):
        tcell_handle_uncaught_exception = BaseHandler.handle_uncaught_exception

        def handle_uncaught_exception(self, request, resolver, exc_info):
            handle_django15_exception(request, *exc_info)
            return tcell_handle_uncaught_exception(self, request, resolver, exc_info)

        BaseHandler.handle_uncaught_exception = handle_uncaught_exception


def _get_middleware_index(middleware_list, after=None, before=None, atIdx=None):
    if after:
        return middleware_list.index(after) + 1 if after in middleware_list else len(middleware_list)
    elif before:
        return middleware_list.index(before) if before in middleware_list else 0
    elif atIdx is not None:
        return atIdx
    else:
        return len(middleware_list)


def _insertMiddleware(middleware_class_string, after=None, before=None, atIdx=None):
    from django.conf import settings

    if hasattr(settings, 'MIDDLEWARE') and settings.MIDDLEWARE:
        middleware_list = list(settings.MIDDLEWARE)
        idx = _get_middleware_index(middleware_list, after, before, atIdx)
        middleware_list.insert(idx, middleware_class_string)
        settings.MIDDLEWARE = tuple(middleware_list)
    else:
        middleware_classes_list = list(settings.MIDDLEWARE_CLASSES)
        idx = _get_middleware_index(middleware_classes_list, after, before, atIdx)
        middleware_classes_list.insert(idx, middleware_class_string)
        settings.MIDDLEWARE_CLASSES = tuple(middleware_classes_list)


def _is_csrf_middleware_enabled():
    from django.conf import settings
    if hasattr(settings, 'MIDDLEWARE'):
        if settings.MIDDLEWARE is None:
            return "django.middleware.csrf.CsrfViewMiddleware" in list(settings.MIDDLEWARE_CLASSES)
        else:
            return "django.middleware.csrf.CsrfViewMiddleware" in list(settings.MIDDLEWARE)
    else:
        return "django.middleware.csrf.CsrfViewMiddleware" in list(settings.MIDDLEWARE_CLASSES)


try:
    import django  # pylint: disable=unused-import

    if TCellAgent.get_agent():
        try:
            from tcell_agent.instrumentation.djangoinst.compatability import django15or16

            if django15or16:
                _dlp_success = False
            else:
                from tcell_agent.instrumentation.djangoinst.dlp import dlp_instrumentation  # noqa pylint: disable=unused-import

                _dlp_success = True
        except ImportError:
            _dlp_success = False
        except Exception as e:
            get_module_logger(__name__).error("Problem importing DLP: {e}".format(e=e))
            get_module_logger(__name__).debug(e, exc_info=True)
            _dlp_success = False

        _instrument()
except ImportError:
    pass
except Exception as e:
    get_module_logger(__name__).debug("Could not instrument django: {e}".format(e=e))
    get_module_logger(__name__).debug(e, exc_info=True)
