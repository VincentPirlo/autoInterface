import os
import pytest
import allure
import logging
import logging.config

from common.method import ApiRequest
from common.getvalue_response import get_value
from config.parse_ini import ParseIni
from config import log_format_conf


p = ParseIni()
a = ApiRequest()
url_prefix = p.geturl("../config/conf.ini", "url", "swagger_url")
logging.config.dictConfig(log_format_conf.LOGGING_DIC)


class TestSwagger:
    @allure.title("1: get inventory")
    @allure.description("这是get inventory")
    @allure.step("get inventory")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('story 1')
    @allure.feature('feature 1')
    def test_get_inventory(self):
        url = url_prefix + '/store/inventory'
        r = a.send_request("get", url)
        logging.getLogger().info('"GET %s %d"' % (url, r.status_code))
        assert r.status_code == 200

    @allure.title("2: post store order")
    @allure.description("这是post store order")
    @allure.step("post store order")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('story 2')
    @allure.feature('feature 2')
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
        logging.getLogger().info('"POST %s %d"' % (url, r.status_code))
        assert r.status_code == 200

    @allure.title("3: get by id")
    @allure.step("get store order by store id")
    @allure.description("这是通过store id获取store order")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('story 3')
    @allure.feature('feature 3')
    def test_get_store_order(self, get_global_data):
        store_id = get_global_data('store_id')
        url = url_prefix + '/store/order/' + str(store_id)
        r = a.send_request("get", url)
        logging.getLogger().info('"GET %s %d"' % (url, r.status_code))
        assert r.status_code == 500


if __name__ == '__main__':
    # pytest.main(['-sv', 'test_swagger.py'])
    pytest.main(['./test_swagger.py', '-s', '--alluredir', '../output/report/allure_data', '--clean-alluredir'])
    os.system('allure generate ./output/report/allure_data -o ../output/report/allure_report --clean')
