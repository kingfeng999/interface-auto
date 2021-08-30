# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/15 5:40 下午
# @Author: zhifeng.qin
# @File: 基础案例合集.py
# @Software: PyCharm

'''
    自动化班编程基础案例讲解
'''

# 将列表中的大写字母改为小写，数字和 None 保持不变
a1 = ['Hello', 'World', 898, None]
a11 = []
for i in a1:
    if isinstance(i, str):  # isinstance 方法可以判断列表元素的类型
        a = i.lower()       # 将大写字母转换为小写
        a11.append(a)       # 如果元素是字符串类型，则加入到新列表中
    else:
        a11.append(i)       # 如果不是字符串类型，则直接加入新的列表中
print(a11)


# 过滤列表中重复的元素，并将重复元素出现的个数打印出来
a2 = [1,1,1,3,3,5,0,0,0,8,8,8,8,10]
li = list(set(a2))      # 集合去重后转换为 list
print(li)
for i in li:
    print('元素{}在列表中出现的次数为：{}次'.format(i, a2.count(i)))


import pytest
import requests

from setting import IP, HEADERS
# 存放的数据是要放到列表中存储
'''
 @pytest.mark.parametrize(,)
 第一个参数:字符串
 第二个参数:列表
 1.[[],[],[]]
 2.[(),(),()]
需求:指定用例的一个描述
通过ids关键字去指定，列表形式传递
读取excel 
1.openpyxl  不仅可以读还可以写(xlsx)
2.xlrd  读
3.xlwd 写

'''
# data_li = [
#     ['yaoyao','yaoyao','登录成功'],
#     ['lwx','yaoyao','帐号不存在'],
#     ['yaoyao','123456','密码错误1111111']
# ]
# data_li = [
#     ('yaoyao','yaoyao','登录成功'),
#     ('lwx','yaoyao','帐号不存在'),
#     ('yaoyao','123456','密码错误')
# ]
data_li = [
    {'accounts': 'yaoyao', 'pwd':'yaoyao','exp':'登录成功'},
    {'accounts': 'lwx', 'pwd': 'yaoyao','exp':'帐号不存在'},
]

ids = ['正向用例','逆向用例']
class TestMtx:

    @pytest.mark.parametrize('dic',data_li,ids=ids)
    def test_login(self, dic):
        '''
        data_li是列表套字典的形式用这个测试用例里面的写法
        :param dic:
        :return:
        '''
        # 构造url地址
        url_login = IP + '/mtx/index.php?s=/index/user/login.html'
        data = {
            'accounts': dic['accounts'],
            'pwd': dic['pwd']
        }
        r = requests.post(url_login,data=data,headers=HEADERS)
        res = r.json()
        # 做断言
        assert res['msg'] == dic['exp']

        @pytest.mark.parametrize('accounts,pwd,exp', data)
        def test_login(self, accounts,pwd,exp):
            '''
            data是列表套列表或者列表套元组的形式用这个测试用例里面的写法
            :param self:
            :param accounts:
            :param pwd:
            :param exp:
            :return:
            '''
            # 构造url地址
            url_login = IP + '/mtx/index.php?s=/index/user/login.html'
            data = {
                'accounts': accounts,
                'pwd': pwd
            }
            r = requests.post(url_login, data=data, headers=HEADERS)
            res = r.json()
            # 做断言
            assert res['msg'] == exp



# if __name__ == '__main__':
#     pytest.main(['-sv','--html=report1.html --self-contained-html'])






