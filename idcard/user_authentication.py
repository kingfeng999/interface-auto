# coding=utf-8
#!/usr/bin/python3
# @Time: 2021/5/8 14:24
# @Author: qinzhifeng
# @File: user_authentication.py
# @Software: PyCharm

from idcard.identity import IdNumber
from idcard import config
import requests
from faker import Faker


# 全局定义 fake 对象
fake = Faker(locale = 'zh_CN')

# 调用 identity 模块，自动生成身份证号
global id_card
id_card = IdNumber.generate_id()




def user_login():
    '''
            使用企业号进行登录，tel 字段根据实际登录账号进行更改，同时适用于新老用户登录注册
    :return:    token, uid
    '''
    global token, uid, phone_num
    phone_num = '19125652444'     # 根据需要更改发布岗位的企业账号
    json = {
        "code": "112334",
        "sign": "5199addf8b86a861c3b47335c7b1864c",
        "tel": phone_num,
        "timestamp": 1611127922,
        "hwid": "53691be5167946f8a6624e3d1f1ffc6f",
        "device": "1",
        "devname": "HONOR HWYAL",
        "ver": "2.20.0"
    }
    resp = requests.post(config.USER_LOGIN_URL, json = json, headers = config.APP_HEADER)
    r = resp.json()
    print("\n","onekey/100 登录接口返回数据".center(20, "‐"),"\n",r)

    # 判断用户登录状态
    if r['ok'] == True:
        print('用户登录成功，登录手机号是：{}'.format(phone_num))

        # 从返回值中获取 token 并返回
        r1 = r.get('data')
        for i in r1:
            print("登录返回__token 是:{},登录返回__uid 是：{}".format({i['token']}, {i['uid']}), "\n")
            token = i['token']
            uid = i['uid']
            return token, uid
    else:
        print('用户登录失败')


def auth_request():
    '''
        用户人工认证请求接口：ringle/user/140
    :return:
    '''

    # 自动生成用户名
    realname = fake.name()
    json = {
        "idurl3": config.IDURL3,
        "idcard": id_card,
        "mobile": phone_num,
        "idurl": config.IDURL1,
        "realname": realname,
        "idurl2": config.IDURL3,
        "token": token,
        "uid": uid
    }
    resp = requests.post(config.AUTH_REQ_URL, json =json, headers = config.APP_HEADER)
    r = resp.json()
    print('实名认证的身份证号为:', id_card)
    print("实名认证姓名为：", realname)

    # 判断生成身份证性别
    if IdNumber(id_card).get_sex() == 0:
        print("生成的身份证性别是：女姓")
    else:
        print("生成的身份证性别是：男姓")

    # 判断用户登录状态
    if r['ok'] == True:
        print('人工实名认证提交成功，ok 的值为：{}'.format(r['ok']))
    else:
        print('人工实名认证提交失败，ok 的值为：{}'.format(r['ok']))


def oa_login():
    '''
        OA 后台登录(暂时不用，以后完善)
    :return:
    '''

    datas = {
        '_csrf':'ku1pp6NfwLOFK6R0Cucj2KBTeYTAoPPgTODeT1MNcinnnB2W6jOfg81alRF_pBqL9iUOtpXYx4cLhr0rBVoHSA==',
        'LoginForm[username]':'qinzhifeng',
        'LoginForm[password]':'yg@123456',
        'LoginForm[verifyCode]':'xupe',
        'LoginForm[rememberMe]':0
    }
    resp = requests.post(config.OA_LOGIN, data = datas, headers = config.WEB_HEADERS)
    # r = resp.content
    r = resp.status_code
    print(r)


def oa_audit():
    '''
        OA 审核(暂时不用，以后完善)
    :return:
    '''

    datas = {
        'id': '1HXk1mZeZgg5oQD9X27dQfjHCjzgLSCHNx',
        'result': 1
    }

    resp = requests.post(config.OA_AUDIT, data = datas, headers = config.WEB_HEADERS)
    r = resp.json()
    print(r)
    if r['message'] == '成功':
        print('实名认证审核通过！')
    else:
        print('实名认证审核不通过！')


if __name__ == '__main__':
    user_login()              # 新老用户登录注册
    auth_request()            # 用户实名认证申请






