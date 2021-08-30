#!/usr/bin/python3
# @Time: 2021/4/1 21:40
# @Author: qinzhifeng
# @File: apiGetCompanyInfo.py
# @Software: PyCharm


'''
    获取公司信息接口的封装
'''

from interface_auto.tools.logger import GetLogger
import interface_auto.config
import requests

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()


class Api_get_company_info():

    def __init__(self):
        logger.info('开始获取公司信息接口的 URL 地址：'.center(50, '-'))
        self.get_company_info_url = "https://gateway-test.svc.kouling.cn/job/100/"
        logger.info(f'获取公司信息接口的 URL 地址是：{self.get_company_info_url}')

    def get_company_info(self):
        json = {
            "pageno": 1,        # 当前页
            "pagenum": 1,       # 分页数
            "token": interface_auto.config.LOGIN_TOKEN,
            "uid": interface_auto.config.LOGIN_UID
        }

        logger.info('准备发起获取公司信息接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.get_company_info_url, json = json, headers = interface_auto.config.HEADERS )
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')

        data = r['data']        # 获得一个 list 数据类型
        for i in data:
            # 将获取的值动态传参到 config 公共变量文件中保存
            interface_auto.config.BACK_COMPANY_ID = i['company_id']
            interface_auto.config.BACK_COMPANY_NAME = i['company_name']
            interface_auto.config.BACK_COMPANY_LOGO = i['company_logo']

        return r

