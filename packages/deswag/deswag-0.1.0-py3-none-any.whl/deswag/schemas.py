"""OpenAPI Schema classes"""
import collections
import jsonschema

import deswag.exceptions as ex
import deswag.openapi as api


Field = collections.namedtuple('Field', ['name', 'constructor'])


class SchemaBase():
    FIELDS = ()

    def __init__(self, source):
        self._source = source

    def data(self):
        ret = {}
        for f in self.FIELDS:
            source = self._source.get(f.name)
            if f.constructor is None:
                ret[f.name] = source
            else:
                ret[f.name] = (None if source is None
                               else f.constructor(source).data())
        return ret


class InfoObjectv2(SchemaBase):
    FIELDS = (
        Field('title', None),
        Field('version', None),
    )


class PathItemObjectv2(SchemaBase):
    FIELDS = (
        Field('$ref', None),
        Field('get', None),
        Field('put', None),
        Field('post', None),
        Field('delete', None),
        Field('options', None),
        Field('head', None),
        Field('patch', None),
        Field('parameters', None),
    )


class PathsObjectv2(SchemaBase):
    def data(self):
        ret = {}
        for k, v in self._source.items():
            if k.startswith('x-'):
                ret[k] = v
            else:
                ret[k] = PathItemObjectv2(v).data()
        return ret


class OpenAPIv2Schema(SchemaBase):
    FIELDS = (
        Field('swagger', None),
        Field('info', InfoObjectv2),
        Field('paths', None),
        Field('host', None),
        Field('basePath', None),
        Field('schemes', None),
        Field('consumes', None),
        Field('produces', None),
        Field('definitions', None),
        Field('parameters', None),
        Field('responses', None),
        Field('securityDefinitions', None),
        Field('security', None),
        Field('tags', None),
        Field('externalDocs', None),
    )

    def __init__(self, source):
        self._validate(source)
        super().__init__(source)

    @staticmethod
    def _validate(source):
        """is this source data valid"""
        try:
            jsonschema.validate(source, api.v2JSONSchema)
        except jsonschema.exceptions.ValidationError as e:
            raise ex.ValidationError(e.message)
