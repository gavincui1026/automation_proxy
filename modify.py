import subprocess

from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://www.example.com":  # 这里url替换成最后提交token的url
        flow.response = http.HTTPResponse.make(
            {"token": capture_token(flow.response.text)}
        )
def capture_token(response):
    # 这里把提取token的逻辑写进去
    pass


