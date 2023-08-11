import os
import pytest

from common.method import ApiRequest
from config.parse_ini import ParseIni
from common.getvalue_response import get_value

p = ParseIni()
a = ApiRequest()
url_prefix = p.geturl("../config/conf.ini", "url", "swagger_url")


class TestSwagger:
    def test_get_inventory(self):
        url = url_prefix + '/store/inventory'
        r = a.send_request("get", url)
        assert r.status_code == 200

    def test_post_order(self, set_global_data):
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

    def test_get_store_order(self, get_global_data):
        store_id = get_global_data('store_id')
        url = url_prefix + '/store/order/' + str(store_id)
        r = a.send_request("get", url)
        assert r.status_code == 200


if __name__ == '__main__':
    # pytest.main(['-sv', 'test_swagger.py'])
    pytest.main(['./test_swagger.py', '-s', '--alluredir', '../output/report/allure_data', '--clean-alluredir'])
    os.system('allure generate ./output/report/allure_data -o ../output/report/allure_report --clean')
