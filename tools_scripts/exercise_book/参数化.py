# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/27 6:00 下午
# @Author: zhifeng.qin
# @File: 参数化.py
# @Software: PyCharm

import pytest
import requests
# 存放的数据是要放到列表中存储
'''
 @pytest.mark.parametrize(,) 第一个参数:字符串，第二个参数:列表
 1.[[],[],[]]
 2.[(),(),()]
 案例说明：列表嵌套字典使用如下参数化方法
'''
# 列表嵌套字典数据类型
data_li = [
    {'accounts': 'yaoyao', 'pwd':'yaoyao','exp':'登录成功'},
    {'accounts': 'lwx', 'pwd': 'yaoyao','exp':'帐号不存在'},
]

# 列表嵌套字典，需要用 ids 关键字指定用例的描述，否则返回 dic0,dic1，可读性不好
ids = ['正向用例','逆向用例']
class TestMtx:

        @pytest.mark.parametrize('dic', data_li, ids = ids)
        def test_login(self, dic):
            '''
            data是列表套列表或者列表套元组的形式用这个测试用例里面的写法
            :return:
            '''
            # 构造url地址
            url_login = IP + '/mtx/index.php?s=/index/user/login.html'
            data = {
                'accounts': dic['accounts'],
                'pwd': dic['pwd']
            }
            r = requests.post(url_login, data=data, headers=HEADERS)
            res = r.json()
            # 做断言
            assert res['msg'] == dic['exp']



# if __name__ == '__main__':
#     pytest.main(['-sv','--html=report1.html --self-contained-html'])