import json

from common.method import ApiRequest
from config.parse_ini import ParseIni
from common.getvalue_response import get_value

p = ParseIni()
a = ApiRequest()
url_prefix = p.geturl("../config/conf.ini", "url", "swagger_url")


class TestOne:
    def test_get_inventory(self):
        url = url_prefix + '/store/inventory'
        r = a.send_request("get", url)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def test_post_order(self):
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
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return get_value(r.text, 'id')

    def test_get_store_order(self):
        url = url_prefix + '/store/order' + self.test_post_order()
        r = a.send_request("get", url)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))


