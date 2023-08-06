# -*- coding: utf-8 -*-
"""
解析请求参数
"""
import functools

from tornado.httputil import parse_body_arguments

from rest_framework.conf import settings
from rest_framework.utils.escape import json_decode
from rest_framework.core.exceptions import ParseError
from rest_framework.utils.functional import import_object
from rest_framework.core.exceptions import ImproperlyConfigured
from rest_framework.utils.transcoder import force_text


class DataAndFiles(object):
    def __init__(self, data, files):
        self.data = data
        self.files = files


@functools.lru_cache()
def get_parsers():
    parsers = []
    for parser_path in settings.PARSER_CLASSES:
        parser = import_object(parser_path)()
        if not getattr(parser, 'media_type'):
            raise ImproperlyConfigured("parser没有定义media_type值: {parser_path}".format(
                parser_path=parser_path)
            )
        parsers.append(parser)

    return parsers


class BaseParser(object):
    media_type = None

    def parse(self, stream, media_type=None, parser_context=None):
        raise NotImplementedError(".parse() must be overridden.")


class JSONParser(BaseParser):
    media_type = 'application/json'

    def parse(self, request):
        try:
            data = json_decode(request.body) if request.body else {}
            return data
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % exc)


class FormParser(BaseParser):
    media_type = 'application/x-www-form-urlencoded'

    def parse(self, request):
        return {k: [force_text(v) for v in vs] if len(vs) > 1 else force_text(vs[-1])
                for k, vs in request.arguments.items() if vs}


class MultiPartParser(BaseParser):
    media_type = 'multipart/form-data'

    def parse(self, request):
        return {k: [force_text(v) for v in vs] if len(vs) > 1 else force_text(vs[-1])
                for k, vs in request.arguments.items() if vs}
