# coding=utf-8
#!/usr/bin/python3
# @Time: 2021-09-02 18:06
# @Author: qinzhifeng
# @File: apiSzguobao.py
# @Software: PyCharm

"""
    发布社招过保岗位，企业预付款
"""

import requests
import interface_auto.config
from interface_auto.tools.logger import GetLogger

# 调用日志工具模块，生成日志对象
logger = GetLogger().get_logger()

class Api_Szguobao():

    def __init__(self):
        logger.info(' 开始获取发布岗位接口的 URL 地址 '.center(50, '-'))
        self.login_url = 'https://gateway-test.svc.kouling.cn/job/102/'
        logger.info('登录接口的 URL 地址是：{}'.format(self.login_url))

    def szguobao_success(self):

        json = {
            "addr": [
                "深圳市"
            ],
            "cnt": 1,
            "company_id": "370",
            "company_logo": "http://cdn3.ringleai.com/media/pic/b2b842c0d55f460c122bd7c6977aece1_w_960_h_960.jpg",
            "desc": "这种行为都能成为一个习惯导致的一个人在家在家躺",
            "education": 7,
            "experience": {
                "max": 10,
                "min": 5
            },
            "extra_desc": "这种行为都能成为一个习惯导致的一个人在家在家躺",
            "hr_info": {
                "email": "76346195@163.com",
                "mobile": "18912428370",
                "qq": "566565555",
                "wechat": "34365555"
            },
            "id": 100304526510000,
            "internship_period": 0,
            "job_name": "是不是要在",
            "job_type": 9000500010000,
            "pay": {
                "max": 6000,
                "min": 4000
            },
            "recruitment_type": "SOCIAL_RECRUITMENT",
            "reward": 150000,
            "reward_pay_type": "EXPIRE",
            "reward_type": "FIXED",
            "reward_year_rate": "0",
            "salary_count": 12,
            "salary_type": "MONTH",
            "token": "5e05cd844f5ae2f8fd93f921fecc4095",
            "type": [
                "STANDARD"
            ],
            "uid": "13UrkCY2tVfdCCm5ChYq3PBPrdkohVzinH",
            "warranty_day": 2,
            "work_day": 0
        }
        logger.info('发布岗位接口的请求，请求的 json 参数是：{}，header 信息是：{}'.format(json, interface_auto.config.HEADERS))
        resp = requests.post(self.login_url, json=json, headers=interface_auto.config.HEADERS)
        r = resp.json()
        logger.info(f'获取的响应值是：{r}')

        '''
            以下代码是打印调试用
        '''
        # print(f"请求结果是：\n{r}")
        # print("请求结果是：\n{}".format(r))

        # 返回数据是字典，可以用 get('data') 或 ['data'] 方式进行获取
        data = r.get('data')
        for i in data:
            # 将登录生成的 token 和 uid，动态传参到 config 文件进行保存，供其他模块进行调用
            interface_auto.config.LOGIN_TOKEN = i['token']
            interface_auto.config.LOGIN_UID = i['uid']

        return r


if __name__ == '__main__':
    login = Api_Login()
    login.login_success()

