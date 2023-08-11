import requests
import json
import os

import parse
import getvalue_response

print(os.path.abspath(__file__))
url = parse.geturl('./config.ini', 'url', 'swagger_url') + '/store/inventory'
# print(url)
r = requests.get(url)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

print(type(r.cookies))
print(r.cookies)


