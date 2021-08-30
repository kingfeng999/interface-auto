# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/2/1 2:44 下午
# @Author: zhifeng.qin
# @File: apiOrder.py
# @Software: PyCharm

import frame_pytest.setting
from frame_pytest.setting import IP, HEADERS


class ApiOrder:
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'


    def order(self,session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',

        }
        resp_order = session.post(self.url,data=data,headers=HEADERS)

        # 302会进行重定向，产生数据动态传递->并把数据放到setting当中(注意)
        # JUMP_URL 是在 setting 文件中定义好的公共变量
        frame_pytest.setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        return resp_order
