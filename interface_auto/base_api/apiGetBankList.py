#!/usr/bin/python3
# @Time: 2021/4/1 11:56
# @Author: qinzhifeng
# @File: apiGetBankList.py
# @Software: PyCharm

'''
    获取银行列表接口的封装
'''

import requests
import interface_auto.config
from interface_auto.tools.logger import GetLogger


# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

class Api_get_bank_list():

    def __init__(self):
        logger.info(' 开始获取银行卡列表接口的 URL 地址 '.center(50, '-'))

        # 定义获取银行卡列表的接口    /pay/121/
        self.get_bankcard_list_url = "https://api3.kouling.cn:14000/ringle/pay/121/"
        logger.info('获取银行卡列表接口的 URL 地址是：{}'.format(self.get_bankcard_list_url))

    def get_bank_list(self):
        '''
            /pay/121/ 获取银行卡列表
        :return:    uuid (银行卡 uuid)
        '''

        json = {
            "card_kind": "PAY",  # 银行卡种类
            "token": interface_auto.config.LOGIN_TOKEN,         # 由 config 文件动态导入 token 等参数
            "uid": interface_auto.config.LOGIN_UID
        }
        logger.info('准备发起获取银行卡列表接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.get_bankcard_list_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')

        data = r.get('data')        # 返回数据类型是字典，因此也可以写成：r['data']
        for i in data:
            interface_auto.config.BACK_UUID = i['uuid']         # // 返回银行卡 uuid 动态传参到保存到 config 公共变量文件中
            logger.info(f'返回 uuid 为：{interface_auto.config.BACK_UUID}')

        return r