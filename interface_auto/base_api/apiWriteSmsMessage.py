#!/usr/bin/python3
# @Time: 2021/4/1 17:49
# @Author: qinzhifeng
# @File: apiWriteSmsMessage.py
# @Software: PyCharm

'''
    验证支付短信接口的封装
'''

from interface_auto.tools.logger import GetLogger
import interface_auto.config
import requests
import time

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

class Api_write_sms_message():

    def __init__(self):
        logger.info('开始获取验证支付短信接口的 URL 地址：'.center(50, '-'))
        self.write_message_url = "https://api3.kouling.cn:14000/ringle/pay/127/"
        logger.info(f'发送支付短信接口的 URL 地址是：{self.write_message_url}')

    def write_sms_message(self):
        json = {
            "token": interface_auto.config.LOGIN_TOKEN,
            "tx_id": interface_auto.config.BACK_TX_ID,
            "uid": interface_auto.config.LOGIN_UID,
            "sms_token": "111111"                       # 支付验证码写死
        }

        logger.info('准备发起验证支付短信接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.write_message_url, json = json, headers = interface_auto.config.HEADERS )
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')
        time.sleep(0.5)
        return r
