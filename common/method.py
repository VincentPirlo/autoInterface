import requests
import allure


class ApiRequest:
    # 方法一
    def send_request(self, method, url, data=None, params=None, **kwargs):
        if method == "get" or method == "GET":
            res = requests.get(url, params=params, **kwargs)
        elif method == "post" or method == "POST":
            res = requests.post(url, data=data, **kwargs)
        elif method == "put" or method == "PUT":
            res = requests.put(url, data=data, **kwargs)
        elif method == "delete" or method == "DELETE":
            res = requests.delete(url, **kwargs)
        else:
            res = None
        return res


    # 方法二
    # def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, json=None, files=None,
    #                   timeout=None):
    #     self.r = requests.request(method, url, data=data, params=params, headers=headers, cookies=cookies, json=json,
    #                               files=files, timeout=timeout)
    #     return self.r

    # 方法三
    # 将get请求行为进行封装
    # @allure.step("发送get请求")
    # def get(self, url, params=None, **kwargs):
    #     return requests.get(url=url, params=params, **kwargs)
    #
    # # 将post请求行为进行封装
    # @allure.step("发送post请求")
    # def post(self, url, data=None, **kwargs):
    #     return requests.post(url=url, data=data, **kwargs)
    #
    # # 将put请求行为进行封装
    # @allure.step("发送put请求")
    # def put(self, url, data=None, **kwargs):
    #     return requests.put(url=url, data=data, **kwargs)
    #
    # # 将delete请求行为进行封装
    # @allure.step("发送delete请求")
    # def delete(self, url, **kwargs):
    #     return requests.delete(url=url, **kwargs)
