import requests


def test_httpbin_http_get():
    url = 'http://httpbin.org/get'
    # headers = 'Accept: application/json'
    r = requests.get(url)
    # 或者a = requests.request(method='GET', url='http://httpbin.org/get')
    # print("\n" + str(r.status_code))
    # print(r.headers)
    # print(r.connection)
    # print(r.cookies)
    # print(r.elapsed)
    # print(r.encoding)
    # print(r.history)
    # print(r.raw)
    # print(r.reason)
    # print(r.request)
    # print(r.url)

    # print(r.text)
    # print(r.content)
    # print(r.is_permanent_redirect)
    # print(r.is_redirect)
    # print(r.links)
    # print(r.next)
    # print(r.ok)

    assert r.status_code == 200


if __name__ == '__main()__':
    test_httpbin_http_get()


