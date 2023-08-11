import requests
import json

import parse
import getvalue_response


url = parse.geturl() + '/store/order'
body = {
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2023-05-23T02:04:29.661Z",
  "status": "approved",
  "complete": 'true'
}

r = requests.post(url, data=body)
# print(r.status_code)
print("origin response content: ", r.text, "\n")
print("value of id is: ", r.json()["id"], "\n")
res = json.dumps(r.json(), indent=2, ensure_ascii=False)
print("json type response: ", res, "\n")
# print("type of res is: ", type(res), "\n")

order_id = getvalue_response.get_value(r.text, 'id')
print(order_id)

url_get_byid = parse.geturl() + "/store/order/" + str(order_id)
r_get_byid = requests.get(url_get_byid)
print(r_get_byid.text)
