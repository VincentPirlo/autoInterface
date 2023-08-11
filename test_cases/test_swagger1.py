import json
import pytest

from common.method import ApiRequest
from config.parse_ini import ParseIni
from common.getvalue_response import get_value

p = ParseIni()
a = ApiRequest()
url_prefix = p.geturl("../config/conf.ini", "url", "swagger_url")


# class TestOne:
def test_get_inventory():
    url = url_prefix + '/store/inventory'
    r = a.send_request("get", url)
    assert r.status_code == 200


def test_post_order(set_global_data):
    url = url_prefix + '/store/order'
    body = {
        "id": 10,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2023-05-23T02:04:29.661Z",
        "status": "approved",
        "complete": 'true'
    }
    r = a.send_request("post", url, body)
    set_global_data('store_id', get_value(r.text, 'id'))
    assert r.status_code == 200


def test_get_store_order(get_global_data):
    store_id = get_global_data('store_id')
    url = url_prefix + '/store/order/' + str(store_id)
    r = a.send_request("get", url)
    assert r.status_code == 200


if __name__ == '__main__':
    pytest.main(['-sv', 'test_swagger1.py'])
