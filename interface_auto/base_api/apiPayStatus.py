#!/usr/bin/python3
# @Time: 2021/4/1 19:36
# @Author: qinzhifeng
# @File: apiPayStatus.py
# @Software: PyCharm

'''
    查询支付状态接口封装
'''

import requests
import interface_auto.config
from interface_auto.tools.logger import GetLogger


logger = GetLogger().get_logger()

class Api_pay_status():

    def __init__(self):
        logger.info('开始获取查询支付状态接口的 URL 地址'.center(50, '-'))
        self.pay_status_url = 'https://api3.kouling.cn:14000/ringle/pay/111/'
        logger.info('查询支付状态接口的 URL 地址是：'.format(self.pay_status_url))

    def pay_status(self):

        json = {
            "token": interface_auto.config.LOGIN_TOKEN,
            "uid": interface_auto.config.LOGIN_UID,
            "orderid": interface_auto.config.BACK_ORDERID      # 订单 ID，依赖于 pay/100，由 config 公共文件动态传参
        }

        logger.info('准备发起发送支付短信接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.pay_status_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{resp}')

        data = r.get('data')
        for i in data:
            if i['status'] == 1:
                logger.info(f"真棒，支付状态正常，status 值为：{i['status']}")
            else:
                logger.info(f"很遗憾，支付状态有异常，status 值为：{i['status']}")

        return r



