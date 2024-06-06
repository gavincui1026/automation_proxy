import subprocess
import time

import requests
from mitmproxy import http
BASE_url = "https://fca-excyd3ecegf7bpcy.a03.azurefd.net/api/MetaClassActionClaimInputFormAPI/triggers/When_a_HTTP_request_is_received/invoke?"
def request(flow: http.HTTPFlow) -> None:
    if BASE_url in flow.request.pretty_url:
        # 修改请求中的json中的reCAPTCHAToken
        flow.request.text = flow.request.text.replace("reCAPTCHAToken", getToken())


def creattask():
    url = 'https://api.capmonster.cloud/createTask'
    data = {
      "clientKey": "679a44b4b2a5d77f7c2aaa8e275ca08f",
      "softId": 44,
      "task": {
        "type": "RecaptchaV3TaskProxyless",
        "websiteURL": "https://www.mnp.ca/en/services/corporate-and-consumer-insolvency/class-action/facebook-claim-form",
        "websiteKey": "6LchOswZAAAAAExqv__mYOvUeAutmKH1O2lM_u57",
        "minScore": "0.9",
        "pageAction": "request_call_back"
      }
    }
    rs = requests.post(url, json=data)
    return rs.json()


def getTask(taskId):
    url = 'https://api.capmonster.cloud/getTaskResult'
    data = {
      "clientKey": "679a44b4b2a5d77f7c2aaa8e275ca08f",
      "taskId": taskId
    }

    rs = requests.post(url, json=data)
    return rs.json()

def getToken():
    taskId = creattask()['taskId']
    while True:
        time.sleep(1)
        rs = getTask(taskId)
        if rs['status'] == 'processing':
            print('processing')
        else:
            return rs['solution']['gRecaptchaResponse']