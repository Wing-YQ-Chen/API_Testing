import requests
import allure
import logging


class AllureRequests:
    def __init__(self, base_url, verify=False, loger=logging.getLogger()):
        """
        类的初始化函数。

        参数：
        - base_url：基础 URL，后续的请求 URL 会在此基础上进行拼接。
        - verify：用于 requests 请求的参数，通常用于控制是否验证 SSL 证书，默认为 False。
        """
        self.base_url = base_url
        self.verify = verify
        self.loger = loger

    def request(self, method, url, **kwargs):
        """
        发送 HTTP 请求的通用函数。

        参数：
        - method：请求方法:``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        - url：请求的具体 URL。
        - **kwargs：传递给 requests.request 的其他参数，如 params、data、json 等。

        函数作用：
        - 发送 HTTP 请求并获取响应。
        - 设置 Allure 报告的标题、标签等信息。
        - 将请求和响应信息以 TSV 格式附加到 Allure 报告中。
        - 返回请求的响应对象。
        """
        sp = requests.request(method=method, url=url, verify=self.verify, **kwargs)
        # allure.dynamic.title(sp.request.url.__str__())
        allure.suite(url)
        allure.dynamic.tag(sp.status_code.__str__())
        allure.dynamic.tag(sp.request.method.__str__())

        rb_text = sp.request.body.__str__().replace('\n', '')

        request_info = f"""
        Request URL \t\t {sp.request.url.__str__()}
        Request Method \t\t {sp.request.method.__str__()}
        Request Headers \t\t {sp.request.headers.__str__()}
        Request Body \t\t {rb_text}
        """

        sp_text = sp.text.__str__().replace('\n', '')

        response_info = f"""
        Response Status \t\t {sp.status_code.__str__()}
        Response Headers \t\t {sp.headers.__str__()}
        Response Content \t\t {sp_text}
        """

        allure.attach(request_info, "Request info", allure.attachment_type.TSV)
        allure.attach(response_info, "Response info", allure.attachment_type.TSV)

        self.loger.info('======================= Request info =======================')
        self.loger.info(request_info)

        self.loger.info('======================= Response info =======================')
        self.loger.info(response_info)

        return sp

    def get(self, params=None, path="", **kwargs):
        """
        发送 GET 请求的函数。

        参数：
        - params：GET 请求的参数。
        - path：请求的路径，会与基础 URL 拼接组成完整的请求 URL。
        - **kwargs：传递给 requests.request 的其他参数。

        函数作用：
        - 构建完整的请求 URL。
        - 调用通用的 request 函数发送 GET 请求。
        - 返回请求的响应对象。
        """
        url = self.base_url + path
        return self.request("get", url, params=params, **kwargs)

    def post(self, json=None, path="", data=None, **kwargs):
        """
        发送 POST 请求的函数。

        参数：
        - json：POST 请求的 JSON 数据。
        - path：请求的路径，会与基础 URL 拼接组成完整的请求 URL。
        - data：POST 请求的数据。
        - **kwargs：传递给 requests.request 的其他参数。

        函数作用：
        - 构建完整的请求 URL。
        - 调用通用的 request 函数发送 POST 请求。
        - 返回请求的响应对象。
        """
        url = self.base_url + path
        return self.request("post", url, data=data, json=json, **kwargs)


if __name__ == "__main__":
    allure_requests = AllureRequests("https://api.example.com")
    response = allure_requests.get("/users")
    print(response.text)
