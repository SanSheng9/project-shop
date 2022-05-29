import datetime
from decimal import Decimal
from dateutil import tz
import dateutil.parser
from django.core.handlers.base import logger
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from uuid import UUID

def method_dispatch(**table):
    @csrf_exempt
    def invalid_method(request, *args, **kwargs):
        logger.warning(
            'Method Not Allowed (%s): %s', request.method, request.path, extra={'status_code': 405, 'request': request})
        return HttpResponseNotAllowed(table.keys())

    @csrf_exempt
    def d(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)

    return d

def format_datetime(date, session=None):
    from api.utils import add_timezone_from_session
    if session is not None:
        return add_timezone_from_session(date, session).replace(microsecond=1).isoformat()
    return (date + datetime.timedelta(hours=10))\
        .replace(tzinfo=tz.tzoffset('VVO', 36000), microsecond=1).isoformat()


def format_date(date):
    return date.isoformat()


def parse_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f%z')


def parse_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y-%m-%d')


def parse_date_utc_convert(date_string):
    try:
        return dateutil.parser.parse(date_string).astimezone(tz.tzutc()).replace(tzinfo=None)
    except:
        return parse_date(date_string)


class JsonEncoder(DjangoJSONEncoder):

    session = None

    def set_session(self, session):
        self.session = session
        return self

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return format_datetime(obj, session=self.session)
        elif isinstance(obj, datetime.date):
            return format_date(obj)
        elif isinstance(obj, UUID):
            return obj.hex
        else:
            return obj.__dict__


def json_response(obj, status=200, session=None):
    return HttpResponse(
        JsonEncoder(ensure_ascii=False).set_session(session).encode(obj),
        content_type="application/json; encoding=utf-8",
        status=status,
    )


def default_json_response(description="", **kwargs):
    obj = {
        "success": True,
        "aiutaCode": 0,
        "description": description,
        "httpCode": 200,
        "extra": None,
    }
    for key, value in kwargs.items():
        obj[key] = value
    return HttpResponse(
        JsonEncoder(ensure_ascii=False).encode(obj),
        content_type="application/json; encoding=utf-8"
    )
