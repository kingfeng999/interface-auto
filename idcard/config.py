# coding = utf-8
#!/usr/bin/python3
# @Time: 2021/5/8 16:46
# @Author: qinzhifeng
# @File: config.py
# @Software: PyCharm

'''
    常量文件
'''

# 客户端 url
USER_LOGIN_URL = 'https://api3.kouling.cn:14000/ringle/onekey/100/'        # 客户端登录
AUTH_REQ_URL = 'https://api3.kouling.cn:14000/ringle/user/140/'            # 人工实名认证
IDURL1 = 'http://cdn51.ringleai.com/user/1FtcdCoGFPCD7rTFRSvW1j8jobYjNGApHV/idcard/fbd747721f951886717261a723513617.jpg'      # 身份证正面
IDURL2 = 'http://cdn51.ringleai.com/user/1FtcdCoGFPCD7rTFRSvW1j8jobYjNGApHV/idcard/d6801a1ac4e6f1f2ace5806579cb53c9.jpg'      # 身份证背面
IDURL3 = 'http://cdn51.ringleai.com/user/1FtcdCoGFPCD7rTFRSvW1j8jobYjNGApHV/idcard/b2e9c0d024a1bfd886c5883a6c313e27.jpg'      # 手持身份证


# 客户端请求头
APP_HEADER = {'Content-Type': 'application/json', 'device': '1', 'version': '2.20.0'}


# web 端 url
OA_LOGIN = 'https://oa2.kouling.cn/sign-in/login'                   # OA 登录 url
OA_AUDIT = 'https://oa2.kouling.cn/forum/cert-realname/save'        # OA 审核 url


# web 端请求头
WEB_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', 'charset':'UTF-8'}


