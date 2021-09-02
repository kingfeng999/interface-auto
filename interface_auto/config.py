#!/usr/bin/python3
# @Time: 2021/2/4 12:07
# @Author: qinzhifeng
# @File: config.py
# @Software: PyCharm

"""
    动态传参的配置文件，包括请求头，token，uid 等等
"""

import os


# 动态生成绝对路径
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)

# header 头部信息
HEADERS = {'Content-Type': 'application/json', 'device': '1', 'version':'2.28.0'}

# 登录接口传过来的 token 和 uid（onekey/100）
LOGIN_TOKEN = None
LOGIN_UID = None

# 注册接口传过来的数据（onekey/100）
REGISTERED_TOKEN = None
REGISTERED_UID = None

# 获取银行卡列表接口传过来的 uuid（pay/121）
BACK_UUID = None

# 银联卡充值接口传过来的数据 （pay/100）
BACK_TX_ID = None               # 交易 ID
BACK_ORDERID = None             # 订单 ID

# 获取公司信息接口传过来的数据
BACK_COMPANY_ID = None          # 公司 ID
BACK_COMPANY_NAME = None        # 公司名称
BACK_COMPANY_LOGO = None        # 公司 Logo






