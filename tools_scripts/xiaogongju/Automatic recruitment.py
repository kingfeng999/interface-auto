#!/usr/bin/python3
# @Time: 2020/12/10 12:10
# @Author: qinzhifeng
# @File: Automatic recruitment.py
# @Software: PyCharm

import requests
import json
import xlrd
import time
import os

"""
自动化实现批量发布招聘岗位脚本
"""

headers = {"Content-Type": "application/json","charset":"UTF-8"}

class Live():
    def __init__(self):
        pass

    @classmethod
    def uid(self):
        url = 'https://api3.kouling.cn:14000/ringle/onekey/100/'
        data = {"code":"112334","sign":"17d69658c5d10ddba29186a7607a6598","tel":13166661519,"timestamp":1604761114,"hwid":"863470032607898","device":"1","devname":"OPPO R9s","ver":"2.10.31"}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        cc = json.loads(res.text)
        return [cc["data"][0]["token"],cc["data"][0]["uid"]]


    def sess(self):
        url = 'https://api3.kouling.cn:14000/ringle/pay/109/'
        pos = self.uid()
        data = {"hwid":"63f24b2c8726492285c13ccd679b53a9","id":'',"pwd":"9459f3e006bfe284220bff3646d5f01b","type":0,"token":pos[0],"uid":pos[1]}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        cc = json.loads(res.text)

        def ll():
            url = 'https://api3.kouling.cn:14000/ringle/user/107/'
            data = {"city": "深圳市", "country": "南山区", "latitude": "22.53956", "longitude": "113.961016",
                    "province": "广东省", "token": pos[0], "town": "高新南七道", "uid": pos[1], "ver": "2.10.31",
                    "village": ""}
            res = requests.post(url=url, data=json.dumps(data), headers=headers)
            cc = json.loads(res.text)
            return cc
        print(ll())
        return [pos[0],pos[1],cc["data"][0]["sessionid"]]



    def job(self,lopo):
        poq = self.sess()
        url = 'https://job2.kouling.cn:20001/job/102/'
        data = {"addr":["深圳市"],"age":{"max":45,"min":18},"company_id":"150","company_name":"平顶山市互通电子商务有限公司","desc":"合适的好的好的好的几点接电话的几点能到记得记得男的女的买的基督教大家觉得","education":2,"experience":{"max":-1,"min":-1},"height":{"max":-1,"min":-1},"job_name":lopo,"orderid":None,"other":[],"pay":{"max":6000,"min":4000},"id":100304501280000,"cnt":1,"reward":100,"sessionid":poq[2],"sex":-1,"skill":[],"token":poq[0],"uid":poq[1]}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        cc = json.loads(res.text)
        return cc

    def jobcount(self):
        posil = os.getcwd()
        polss = os.listdir(posil)
        for oiko in polss:
            if oiko.endswith('.xlsx'):
                sper = os.path.join(posil, oiko)
        test = xlrd.open_workbook(os.path.join(posil, sper))
        test = test.sheet_by_name("Sheet2")
        liec = test.ncols
        sug = []
        for lie in range(liec):
            ber = test.col_values(lie)
            for ter in ber:
                if ter == '':
                    continue
                sug.append(ter)
        return sug

a = Live()
s = a.jobcount()

for lopo in s:
    print(a.job(lopo))
    time.sleep(1)

input("批量发布招聘已完成，按Enter键退出：")

