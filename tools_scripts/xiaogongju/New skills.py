#!/usr/bin/python3
# @Time: 2020/12/10 14:29
# @Author: qinzhifeng
# @File: New skills.py
# @Software: PyCharm

import requests
import json
import xlrd
import os

'''
自动新建指定技能
'''

headers = {"Content-Type": "application/json","charset":"UTF-8"}

class Live():
    def __init__(self):
        pass
    @classmethod
    def uid(self,ppp):
        vvv = 11111111111+ppp
        print("手机号是：",vvv)
        url = 'https://api3.kouling.cn:14000/ringle/onekey/100/'
        vvv = str(vvv)
        data = {"code":"112334","sign":"17d69658c5d10ddba29186a7607a6598","tel":vvv,"timestamp":1604761114,"hwid":"863470032607898","device":"1","devname":"OPPO R9s","ver":"2.10.31"}
        res = requests.post(url=url,data=json.dumps(data),headers=headers)
        cc = json.loads(res.text)
        return [cc["data"][0]["token"],cc["data"][0]["uid"]]

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

    def jineng(self,ppp,potys):
        pos = self.uid(ppp)
        url = 'https://api3.kouling.cn:14000/ringle/user/102/'
        print("建立的技能是：",potys)
        data = {"avatar":"http://cdn3.ringleai.com/media/avatar/b56f0f8bd24f2b1a7c18b3a48cc090dc.jpg","dayflag":1111111,"desc":"这是一个批量任务跑出来的服务详情*3，这是一个批量任务跑出来的服务详情*3，这是一个批量任务跑出来的服务详情*3","desc_voice_duration":0,"etime":"23:59","isdefaultinfo":0,"isfree":1,"isrealavatar":0,"isshowrealname":0,"nick":"这是批量设置的昵称","password":potys,"isopenmobile":1,"picurllist":[],"price":0,"onlyrecvrealname":0,"remote_service_price":0,"sex":-1,"sound_effect":0,"stime":"07:00","token":pos[0],"uid":pos[1],"video_price":0,"visiting_service_price":0}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        cc = json.loads(res.text)
        return cc

a = Live()
polf = a.jobcount()
ppp = 0
for potys in polf:
    ppp = ppp+1
    jieguo = a.jineng(ppp,potys)
    print(jieguo)
