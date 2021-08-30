#!/usr/bin/python3
# @Time: 2021/4/1 17:05
# @Author: qinzhifeng
# @File: apiSendMessageCode.py
# @Software: PyCharm

'''
    发送支付短信接口的封装
'''

from interface_auto.tools.logger import GetLogger
import interface_auto.config
import requests

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()


class Api_send_message_code():

    def __init__(self):
        logger.info('开始获取发送支付短信接口的 URL 地址：'.center(50, '-'))
        self.send_message_url = "https://api3.kouling.cn:14000/ringle/pay/126/"
        logger.info(f'发送支付短信接口的 URL 地址是：{self.send_message_url}')

    def send_message_code(self):
        logger.info(f'传入的 tx_id 为：{interface_auto.config.BACK_TX_ID}')
        json ={
            "token": interface_auto.config.LOGIN_TOKEN,
            "tx_id": interface_auto.config.BACK_TX_ID,      # 传交易 ID，依赖于 pay/100
            "uid": interface_auto.config.LOGIN_UID
        }

        logger.info('准备发起发送支付短信接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.send_message_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')
        return r

