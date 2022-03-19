# -*- coding:utf-8 -*-
import requests
import sys
import time

# 统一身份认证系统的用户名和密码
username = "19721629"
password = "46630e2b4e0faec42fe6c62279cae76ce1cec239fffe4d167306dbe95a23e8572ea20fa97c6ecda2aecafcec557704ea56df496a48e01693d78a053656b50f4fc3b80e091c0a473954420d409aa86407cf13db395dec85a1813ccde1de9dddd2019ef02990aedbc971723f90e4ed91402e69ba562b924ea9558311f16c941915"
# 我们都习惯访问百度，那就这样吧
BAIDU = "http://www.baidu.com"


def log(message):
    CURRENT_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(CURRENT_TIME + ' - ' + str(message))


if __name__ == '__main__':
    try:
        parameters = requests.get(BAIDU, timeout=10).text
        serach_index = parameters.find(".jsp?")
        if serach_index == -1:
            log("Already Login!")
            sys.exit(0)
        queryString = parameters[serach_index + 5:-12]
    except requests.exceptions.RequestException:
        log("Timeout or other network error!")
        sys.exit(-1)
    login_url = "http://10.10.9.9:8080/eportal/InterFace.do?method=login"
    payload = {
        'userId': username,
        'password': password,
        'service': 'shu',
        'queryString': queryString,
        'operatorPwd': '',
        'operatorUserId': '',
        'vaildcode': '',
        'passwordEncrypt': 'true'
    }
    # 发送 POST 请求，提交登录表单
    response = requests.post(login_url, data=payload)
    # print(response.text)
    # 结果判断
    if response.text.find("success") >= 0:
        log("login success!")
        sys.exit(0)
    else:
        log("login failure!")
        sys.exit(-1)
