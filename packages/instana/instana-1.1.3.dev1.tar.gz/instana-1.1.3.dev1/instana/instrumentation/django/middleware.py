from __future__ import absolute_import

import sys

import opentracing as ot
import opentracing.ext.tags as ext
import wrapt

from ...log import logger
from ...tracer import internal_tracer as tracer

DJ_INSTANA_MIDDLEWARE = 'instana.instrumentation.django.middleware.InstanaMiddleware'

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class InstanaMiddleware(MiddlewareMixin):
    """ Django Middleware to provide request tracing for Instana """
    def __init__(self, get_response=None):
        logger.debug("InstanaMiddleware.__init__ called")
        self.get_response = get_response
        self

    def process_request(self, request):
        logger.debug("InstanaMiddleware.process_request called")
        try:
            env = request.environ
            ctx = None
            if 'HTTP_X_INSTANA_T' in env and 'HTTP_X_INSTANA_S' in env:
                ctx = tracer.extract(ot.Format.HTTP_HEADERS, env)

            self.scope = tracer.start_active_span('django', child_of=ctx)

            self.scope.span.set_tag(ext.HTTP_METHOD, request.method)
            if 'PATH_INFO' in env:
                self.scope.span.set_tag(ext.HTTP_URL, env['PATH_INFO'])
            if 'QUERY_STRING' in env:
                self.scope.span.set_tag("http.params", env['QUERY_STRING'])
            if 'HTTP_HOST' in env:
                self.scope.span.set_tag("http.host", env['HTTP_HOST'])
        except Exception:
            logger.debug("Instana middleware @ process_response", exc_info=True)

    def process_response(self, request, response):
        logger.debug("InstanaMiddleware.process_response called")
        try:
            if self.scope is not None:
                if 500 <= response.status_code <= 511:
                    self.scope.span.set_tag("error", True)
                    ec = self.scope.span.tags.get('ec', 0)
                    if ec is 0:
                        self.scope.span.set_tag("ec", ec+1)

                self.scope.span.set_tag(ext.HTTP_STATUS_CODE, response.status_code)
                tracer.inject(self.scope.span.context, ot.Format.HTTP_HEADERS, response)
        except Exception:
            logger.debug("Instana middleware @ process_response", exc_info=True)
        finally:
            self.scope.close()
            self.scope = None
            return response

    def process_exception(self, request, exception):
        logger.debug("InstanaMiddleware.process_exception called")
        if self.scope is not None:
            self.scope.span.set_tag(ext.HTTP_STATUS_CODE, 500)
            self.scope.span.set_tag('http.error', str(exception))
            self.scope.span.set_tag("error", True)
            ec = self.scope.span.tags.get('ec', 0)
            self.scope.span.set_tag("ec", ec+1)
            self.scope.close()


def load_middleware_wrapper(wrapped, instance, args, kwargs):
    logger.debug("load_middleware_wrapper called")
    try:
        from django.conf import settings

        # Django >=1.10 to <2.0 support old-style MIDDLEWARE_CLASSES so we
        # do as well here
        if hasattr(settings, 'MIDDLEWARE'):
            logger.debug("found settings.MIDDLEWARE")
            if DJ_INSTANA_MIDDLEWARE in settings.MIDDLEWARE:
                logger.debug("djmw already in MIDDLEWARE")
                return wrapped(*args, **kwargs)

            # Save the list of middleware for Snapshot reporting
            logger.debug("saving djmw list for snapshot reporting")
            tracer.sensor.meter.djmw = settings.MIDDLEWARE

            if type(settings.MIDDLEWARE) is tuple:
                logger.debug("MIDDLEWARE is a tuple")
                settings.MIDDLEWARE = (DJ_INSTANA_MIDDLEWARE,) + settings.MIDDLEWARE
            elif type(settings.MIDDLEWARE) is list:
                logger.debug("MIDDLEWARE is a list")
                settings.MIDDLEWARE = [DJ_INSTANA_MIDDLEWARE] + settings.MIDDLEWARE
            else:
                logger.warn("Instana: Couldn't add InstanaMiddleware to Django")

            logger.debug("middleware should be set.  this is the list:")
            logger.debug(settings.MIDDLEWARE)

        elif hasattr(settings, 'MIDDLEWARE_CLASSES'):
            logger.debug("found settings.MIDDLEWARE_CLASSES")
            if DJ_INSTANA_MIDDLEWARE in settings.MIDDLEWARE_CLASSES:
                logger.debug("djmw already in MIDDLEWARE_CLASSES")
                return wrapped(*args, **kwargs)

            # Save the list of middleware for Snapshot reporting
            logger.debug("saving djmw list for snapshot reporting")
            tracer.sensor.meter.djmw = settings.MIDDLEWARE_CLASSES

            if type(settings.MIDDLEWARE_CLASSES) is tuple:
                logger.debug("MIDDLEWARE_CLASSES is a tuple")
                settings.MIDDLEWARE_CLASSES = (DJ_INSTANA_MIDDLEWARE,) + settings.MIDDLEWARE_CLASSES
            elif type(settings.MIDDLEWARE_CLASSES) is list:
                logger.debug("MIDDLEWARE_CLASSES is a list")
                settings.MIDDLEWARE_CLASSES = [DJ_INSTANA_MIDDLEWARE] + settings.MIDDLEWARE_CLASSES
            else:
                logger.warn("Instana: Couldn't add InstanaMiddleware to Django")

            logger.debug("middleware should be set.  this is the list:")
            logger.debug(settings.MIDDLEWARE_CLASSES)
        else:
            logger.warn("Instana: Couldn't find middleware settings")

        logger.debug("Returning wrapped")
        return wrapped(*args, **kwargs)
    except Exception:
            logger.warn("Instana: Couldn't add InstanaMiddleware to Django", exc_info=True)


try:
    logger.debug("checking for django in sys.modules")
    if 'django' in sys.modules:
        logger.debug("django found in sys.modules")
        wrapt.wrap_function_wrapper('django.core.handlers.base', 'BaseHandler.load_middleware', load_middleware_wrapper)
        logger.debug("wrapper set")
except Exception:
    logger.debug("middleware outerblock exception happeneed", exc_info=True)
    pass
