#!/usr/bin/python3
# @Time: 2021/2/4 17:00
# @Author: qinzhifeng
# @File: test_registered.py
# @Software: PyCharm


'''
    注册接口测试
'''
from interface_auto.base_api.apiRegistered import ApiRegistered
import allure

class TestRegistered():
    '''
           Severity定制详解
           Allure中对严重级别的定义：
           1、 Blocker 级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
           2、 Critical 级别：临界缺陷（ 功能点缺失）
           3、 Normal 级别：普通缺陷（数值计算错误）
           4、 Minor 级别：次要缺陷（界面错误与UI需求不符）
           5、 Trivial 级别：轻微缺陷（必输项无提示，或者提示不规范）
       '''

    @allure.feature('注册功能')
    @allure.story('用户注册正常')
    @allure.title('用户能正常注册')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @allure.severity('Blocker')
    def test_registered(self):
        '''
        用户注册的测试用例
        :return:
        '''
        resp = ApiRegistered().registered_success()
        assert resp['ok'] == True

