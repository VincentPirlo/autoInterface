import yaml
from common.method import ApiRequest
from config.parse_ini import ParseIni

def yaml_load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


data = yaml_load('test_2.yml')
print(type(data), data)
print(data['version'])
print(data['apiinface'])
print(data['apiinface'][0]['/pet inventory']['method'])

a = ApiRequest()
p = ParseIni()
url = p.geturl('../../config/conf.ini', 'url', 'swagger_url') + data['apiinface'][0]['/pet inventory']['url']
print(url)

r = a.send_request(data['apiinface'][0]['/pet inventory']['method'], url)
print(r.status_code)

r2 = a.send_request("get", "https://petstore3.swagger.io/api/v3/store/inventory")
print(r2.status_code)

