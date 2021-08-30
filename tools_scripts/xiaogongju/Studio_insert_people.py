#!/usr/bin/python3
# @Time: 2020/12/10 12:08
# @Author: qinzhifeng
# @File: Studio_insert_people.py
# @Software: PyCharm

import requests
import json

'''
自动实现直播间插入人数
'''

ooo = int(input("请输入直播间ID号："))
aa = int(input("请输入目标直播间人数："))


headers = {"Content-Type": "application/json","charset":"UTF-8"}

class Live():
    def __init__(self):
        pass
    @classmethod
    def uid(self,ppp):
        vvv = 11111111111+ppp
        url = 'https://api3.kouling.cn:14000/ringle/onekey/100/'
        vvv = str(vvv)
        data = {"code":"112334","sign":"17d69658c5d10ddba29186a7607a6598","tel":vvv,"timestamp":1604761114,"hwid":"863470032607898","device":"1","devname":"OPPO R9s","ver":"2.10.31"}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        cc = json.loads(res.text)
        return [cc["data"][0]["token"],cc["data"][0]["uid"]]

    def pid(self,ppp):
        url = 'https://api3.kouling.cn:14000/ringle/onekey/102/'
        a = self.uid(ppp)
        data = {"hwid":"863470032607898","device":"1","devname":"OPPO R9s","ver":"2.10.31","token":a[0],"uid":a[1]}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        cc = json.loads(res.text)
        return [cc["data"][0]["id"],a[0],a[1]]

    def live(self,ppp,ooo):
        url = 'https://api3.kouling.cn:17000/ringle/live/join_live/'
        a =self.pid(ppp)
        data = {"live_id":ooo,"pid":a[0],"token":a[1],"uid":a[2]}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        cc = json.loads(res.text)
        return cc



a = Live()
for ccc in range(0,aa):
    ru = a.live(ccc, ooo)
    print(ru)
