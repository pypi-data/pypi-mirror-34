from tornado_battery.exception import ClientException
from marshmallow import Schema
import functools
import ujson


def schema(query=None, form=None, json=None, reply=None):

    def _load_query(handler, schema):
        data = {}
        for key, value in handler.request.query_arguments.items():
            if not key.endswith('[]'):
                data[key] = value[-1]
            else:
                data[key] = value
        return schema.load(data).data

    def _load_form(handler, schema):
        data = {}
        for key, value in handler.request.body_arguments.items():
            if not key.endswith('[]'):
                data[key] = value[-1]
            else:
                data[key] = value
        return schema.load(data).data

    def _load_json(handler, schema):
        content_type = handler.request.headers.get('Content-Type')
        if not content_type.startswith('application/json'):
            raise ClientException('invalid content-type')
        try:
            data = ujson.loads(handler.request.body)
        except Exception:
            raise ClientException('invalid content format')
        else:
            return schema.load(data).data

    def wrapper(function):

        @functools.wraps(function)
        async def f(handler, *args, **kwargs):
            if query and isinstance(query, Schema):
                kwargs.update({'query': _load_query(handler, query)})
            if form and isinstance(form, Schema):
                kwargs.update({'form': _load_form(handler, form)})
            if json and isinstance(json, Schema):
                kwargs.update({'json': _load_json(handler, json)})
            retval = await function(handler, *args, **kwargs)

            if reply and isinstance(reply, Schema):
                assert isinstance(retval, dict)
                handler.set_header('Content-Type',
                                   'application/json; charset=UTF-8')
                data = reply.dump(retval['data']).data
                return handler.finish(dict(code=retval.get('code', 0),
                                           msg=retval.get('msg', ''),
                                           data=data))

            return retval
        return f

    return wrapper
