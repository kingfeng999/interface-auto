#!/usr/bin/python3
# @Time: 2021/2/4 21:07
# @Author: qinzhifeng
# @File: apiLogout.py
# @Software: PyCharm

import requests
import interface_auto.config
from interface_auto.tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiLogout():

    def __init__(self):
        logger.info(' 开始获取退出登录接口的 URL '.center(50,'-'))
        self.logout_url = 'https://api3.kouling.cn:14000/ringle/user/115/'
        logger.info('退出登录接口的 URL 是：{}'.format(self.logout_url))
        # logger.info(f"传入token: {interface_auto.config.LOGIN_TOKEN}，传入uid: {interface_auto.config.LOGIN_UID}")

    def logout_success(self):
        json = {
            "token": interface_auto.config.LOGIN_TOKEN,
            "uid": interface_auto.config.LOGIN_UID
        }
        logger.info('准备发起退出登录接口的请求，请求参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.logout_url, json = json, headers = interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'退出登录获取的响应值是：{r}')
        return r