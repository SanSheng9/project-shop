import json

from .error_service import ErrorException, FIELD_REQUIRED
from .json_service import json_response


def parse_json(json_string):
    if isinstance(json_string, str):
        if not json_string:
            json_string = '{}'
        return json.loads(json_string)
    else:
        json_string = json_string.decode('utf-8')
        if not json_string:
            json_string = '{}'
        return json.loads(json_string)
        
class BaseRequestEntity:

    def __init__(self, json_string):
        self.__dict__ = parse_json(json_string)

    @staticmethod
    def parse_array(json_string):
        if isinstance(json_string, str):
            return json.loads(json_string)
        else:
            return json.loads(json_string.decode('utf-8'))

    @staticmethod
    def raise_on_null(**kw):
        extra = 'Отсутствующие параметры: '
        is_exception_needed = False
        for key, value in kw.items():
            if value is None or (isinstance(value, str) and len(value) == 0):
                extra += str(key) + ' '
                is_exception_needed = True
        if is_exception_needed:
            raise ErrorException(FIELD_REQUIRED, extra)

    @staticmethod
    def raise_on_null_or_zero(**kw):
        extra = 'Отсутствующие параметры: '
        is_exception_needed = False
        for key, value in kw.items():
            if value is None or (isinstance(value, int) and value == 0):
                extra += str(key) + ' '
                is_exception_needed = True
        if is_exception_needed:
            raise ErrorException(FIELD_REQUIRED, extra)