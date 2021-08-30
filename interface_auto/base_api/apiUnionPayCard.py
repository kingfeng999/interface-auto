#!/usr/bin/python3
# @Time: 2021/4/1 15:56
# @Author: qinzhifeng
# @File: apiUnionPayCard.py
# @Software: PyCharm

'''
    银联卡充值接口的封装
'''

from interface_auto.tools.logger import GetLogger
import interface_auto.config
import requests
import time

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

class Api_union_pay_card():

    def __init__(self):
        logger.info('开始获取银联卡充值下单接口的 URL 地址 '.center(50, '-'))
        self.union_pay_card_url = "https://api3.kouling.cn:14000/ringle/pay/100/"
        logger.info(f'银联卡充值下单接口的地址是：{self.union_pay_card_url}')

    def union_pay_card(self):
        '''
            通过银联卡充值（下单）: pay/100
        :return:
        '''

        json ={
            "appid": "",                                        # 应用 ID（必填）
            "card_uuid": interface_auto.config.BACK_UUID,       # 银行卡编号，channelid 为 4 时为必填，/pay/121/ 接口返回中获取（可选）
            "channelid": 4,                                     # 充值渠道（1、支付宝， 2、微信， 3、微信小程序， 4、银联卡快捷支付）--- 必填
            "cnt": 1,                                           # 商品数量（必填）
            "device_info": "6353",                              # 设备号（必填）
            "goods": "10000",                                   # 商品 ID（必填）
            "mchid": "",                                        # 商户号（必填）
            "noncestr": "654315315",                            # 随机字符串（必填）
            "price": 300000,                                    # 商品单价（必填）
            "sign": "35321351315132",                           # 签名 md5（必填）
            "token": interface_auto.config.LOGIN_TOKEN,         # 登录返回 token（必填）
            "total_free": 300000,                               # 订单总金额，以分为单位（必填）
            "type": 6,                                          # 充值类别（0普通，1红包，2通话中充值，3培训费用, 4订单付费，5保证金）--- 必填
            "uid": interface_auto.config.LOGIN_UID              # 用户 ID（必填）
        }
        logger.info('准备发起银联卡充值接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.union_pay_card_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')

        data = r['data']
        for i in data:
            # 返回订单ID和交易ID数据动态传参到保存到 config 公共变量文件中
            interface_auto.config.BACK_TX_ID = i['tx_id']
            interface_auto.config.BACK_ORDERID = i['orderid']
            logger.info(f'传入的 tx_id 为：{interface_auto.config.BACK_TX_ID}')
            logger.info(f'传入的 orderid 为：{interface_auto.config.BACK_ORDERID}')
            time.sleep(0.5)
        return r


