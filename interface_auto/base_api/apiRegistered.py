#!/usr/bin/python3
# @Time: 2021/2/4 16:54
# @Author: qinzhifeng
# @File: apiRegistered.py
# @Software: PyCharm

'''
    注册接口的封装
'''

import requests
from faker import Faker
from interface_auto.tools.logger import GetLogger
import interface_auto.config

logger = GetLogger().get_logger()
faker = Faker(locale = 'zh_CN')

class ApiRegistered():

    def __init__(self):
        logger.info(' 开始获取注册接口的 URL 地址 '.center(50, '-'))
        self.registered_url = 'https://api3.kouling.cn:14000/ringle/onekey/100/'
        logger.info('注册接口的 URL 地址是：{}'.format(self.registered_url))

    # 用户成功注册
    def registered_success(self):
        '''
            用户注册
        :return:
        '''
        phone = faker.phone_number()
        logger.info('自动生成的注册手机号是：{}'.format(phone))
        json = {
            "code": "112334",
            "sign": "5199addf8b86a861c3b47335c7b1864c",
            "tel": phone,
            "timestamp": 1611127922,
            "hwid": "53691be5167946f8a6624e3d1f1ffc6f",
            "device": "1",
            "devname": "HONOR HWYAL",
            "ver": "2.17.0"
        }
        logger.info('准备发起注册接口的请求，请求参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.registered_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')
        r1 = r.get('data')

        # 在响应结果中循环遍历，并返回响应数据 r，token 和 uid
        # 动态生成的 token 和 uid 传到 config 文件中
        for i in r1:
            interface_auto.config.REGISTERED_TOKEN = i['token']
            interface_auto.config.REGISTERED_UID = i['uid']
            logger.info('注册生成 token -- {}'.format(interface_auto.config.REGISTERED_TOKEN))
            logger.info('注册生成 uid -- {}'.format(interface_auto.config.REGISTERED_UID))
        return r

# if __name__ == '__main__':
#     a = ApiRegistered().registered_success()
#     print(a)