#!/usr/bin/python3
# @Time: 2021/4/1 22:09
# @Author: qinzhifeng
# @File: apiAddJob.py
# @Software: PyCharm

'''
    发布岗位接口的封装
'''

from interface_auto.tools.logger import GetLogger
import interface_auto.config
import requests
from faker import Faker

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

# 创建 faker 对象
faker = Faker(locale='zh_CN')


class Api_add_job():

    def __init__(self):
        logger.info('开始获取发布岗位接口的 URL 地址：'.center(50, '-'))
        self.add_job_url = "https://gateway-test.svc.kouling.cn/job/102/"
        logger.info(f'发送支付短信接口的 URL 地址是：{self.add_job_url}')

    def add_two_type_job(self):
        '''
            发布标准 + 极速岗位
        :return:
        '''

        # 随机生成岗位信息
        name = faker.words(1)
        job_name = ''.join(name) + '：' + '标准加极速岗'
        json = {
            "addr": ["深圳市"],
            "age": {
                "max": 45,
                "min": 18
            },
            "cnt": 2,
            "company_id": interface_auto.config.BACK_COMPANY_ID,
            "company_logo": interface_auto.config.BACK_COMPANY_LOGO,
            "company_name": interface_auto.config.BACK_COMPANY_NAME,
            "desc": "劳动最光荣加班最光荣购物最好玩不信你来试试吧",
            "education": 2,
            "experience": {
                "max": 5,
                "min": 3
            },
            "height": {
                "max": -1,
                "min": -1
            },
            "id": 100304501310000,
            "job_name": job_name,
            "job_type": 9000300020000,
            "orderid": interface_auto.config.BACK_ORDERID,
            "other": ["你比较牛逼", "可能长得不是一般的帅", "形象气质佳"],
            "pay": {
                "max": 6000,
                "min": 4000
            },
            "reward": 150000,
            "sex": -1,
            "skill": ["IOS开发"],
            "token": interface_auto.config.LOGIN_TOKEN,
            "type": ["STANDARD", "FAST"],
            "uid": interface_auto.config.LOGIN_UID,
            "warranty_day": "2"
        }



        logger.info('准备发起发布岗位接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.add_job_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')
        # logger.info(f'发布的岗位名称是：{job_name}')

        return r


    def add_standard_job(self):
        '''
            仅发布标准岗位
        :return:
        '''

        # 随机生成岗位信息
        name = faker.words(1)
        job_name = ''.join(name) + '：' + '仅标准岗'

        json = {
            "addr": ["深圳市"],
            "age": {"max": 45, "min": 18},
            "cnt": 2,
            "company_id": interface_auto.config.BACK_COMPANY_ID,
            "company_logo": interface_auto.config.BACK_COMPANY_LOGO,
            "company_name": interface_auto.config.BACK_COMPANY_NAME,
            "desc": "劳动最光荣加班最光荣购物最好玩不信你来试试吧",
            "education": 2,
            "experience": {"max": 5, "min": 3},
            "height": {"max": -1, "min": -1},
            "id": 100304501310000,
            "job_name": job_name,
            "job_type": 9000300020000,
            "orderid": interface_auto.config.BACK_ORDERID,
            "other": ["你比较牛逼", "可能长得不是一般的帅", "形象气质佳"],
            "pay": {"max": 6000, "min": 4000},
            "reward": 150000,
            "sex": -1,
            "skill": ["IOS开发"],
            "token": interface_auto.config.LOGIN_TOKEN,
            "type": ["STANDARD"],
            "uid": interface_auto.config.LOGIN_UID,
            "warranty_day": "2"
        }

        logger.info('准备发起发布岗位接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.add_job_url, json=json, headers=interface_auto.config.HEADERS)
        r = resp.json()
        logger.info('获取的响应值是：'.format(r))
        return r


    def add_fast_job(self):
        '''
            仅发布极速岗位
        :return:
        '''

        # 随机生成岗位信息
        name = faker.words(1)
        job_name = ''.join(name) + '：' + '仅极速岗'

        json = {
            "addr": ["深圳市"],
            "age": {"max": 45, "min": 18},
            "company_id": interface_auto.config.BACK_COMPANY_ID,
            "company_logo": interface_auto.config.BACK_COMPANY_LOGO,
            "company_name": interface_auto.config.BACK_COMPANY_NAME,
            "desc": "劳动最光荣加班最光荣购物最好玩不信你来试试吧",
            "education": 2,
            "experience": {"max": 5, "min": 3},
            "height": {"max": -1, "min": -1},
            "id": 100304501310000,
            "job_name": job_name,
            "other": ["你比较牛逼", "可能长得不是一般的帅", "形象气质佳"],
            "pay": {"max": 6000, "min": 4000},
            "sex": -1,
            "skill": ["IOS开发"],
            "token": interface_auto.config.LOGIN_TOKEN,
            "type": ["FAST"],
            "uid": interface_auto.config.LOGIN_UID
        }

        logger.info('准备发起发布岗位接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.add_job_url, json=json, headers=interface_auto.config.HEADERS)
        r = resp.json()
        logger.info('获取的响应值是：'.format(r))
        return r



