import json
import jsonpath


def get_value(data, key):
    json_data = json.loads(data)
    value = jsonpath.jsonpath(json_data, '$..{0}'.format(key))
    return value[0]
