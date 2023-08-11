import json

from common.method import ApiRequest
from config.parse_ini import ParseIni

p = ParseIni()

url = p.geturl("../config/conf.ini", "url", "swagger_url") + '/store/inventory'
a = ApiRequest()
# 或 r = a.send_request(method="get", url=url, params=None)
# 或 r = a.send_request(method="get", url=url)
r = a.send_request("get", url)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))


