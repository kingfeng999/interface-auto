#!/usr/bin/python3
# @Time: 2020/12/10 12:06
# @Author: qinzhifeng
# @File: add_lingdui.py
# @Software: PyCharm

import requests
import json
import time

"""
自动化实现增加领队成员脚本
"""

def uid(p):
    vvv = 11111111111 + p
    print("手机号是：", vvv)
    headers = {"Content-Type": "application/json", "charset": "UTF-8"}
    url = 'https://api3.kouling.cn:16001/ringle/web/register'
    vvv = str(vvv)
    data = {"op_type":1,"mobile":vvv,"sms_code":"112334","code":"CdY5TEwL"}
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    cc = json.loads(res.text)
    return cc

for a in range(0,2):
    print(uid(a))
    time.sleep(2)


