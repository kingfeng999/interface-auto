#!/usr/bin/python3
# @Time: 2021/2/4 14:16
# @Author: qinzhifeng
# @File: apiLogin.py
# @Software: PyCharm

'''
    登录接口的封装
'''

import requests
import interface_auto.config
from interface_auto.tools.logger import GetLogger

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

class Api_Login():

    def __init__(self):
        logger.info(' 开始获取登录接口的 URL 地址 '.center(50,'-'))
        self.login_url = 'https://api3.kouling.cn:14000/ringle/onekey/100/'
        logger.info('登录接口的 URL 地址是：{}'.format(self.login_url))

    def login_success(self):
        json = {
            "code": "112334",
            "sign": "5199addf8b86a861c3b47335c7b1864c",
            "tel": "13802282483",
            "timestamp": 1611127922,
            "hwid": "53691be5167946f8a6624e3d1f1ffc6f",
            "device": "1",
            "devname": "HONOR HWYAL",
            "ver": "2.17.0"
        }
        logger.info('准备发起登录接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.login_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')

        # 返回数据是字典，可以用 get('data') 或 ['data'] 方式进行获取
        data = r.get('data')
        for i in data:
            # 将登录生成的 token 和 uid，动态传参到 config 文件进行保存，供其他模块进行调用
            interface_auto.config.LOGIN_TOKEN = i['token']
            interface_auto.config.LOGIN_UID = i['uid']

        return r