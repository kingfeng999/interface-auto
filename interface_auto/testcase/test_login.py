#!/usr/bin/python3
# @Time: 2021/2/4 14:16
# @Author: qinzhifeng
# @File: test_login.py
# @Software: PyCharm

from interface_auto.base_api.apiLogin import Api_Login
import allure
import pytest

'''
    登录接口测试
'''

class TestLogin():
    '''
        Severity定制详解
        Allure中对严重级别的定义：
        1、 Blocker 级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
        2、 Critical 级别：临界缺陷（ 功能点缺失）
        3、 Normal 级别：普通缺陷（数值计算错误）
        4、 Minor 级别：次要缺陷（界面错误与UI需求不符）
        5、 Trivial 级别：轻微缺陷（必输项无提示，或者提示不规范）
    '''

    @allure.feature('登录功能')
    @allure.story('正常登录场景')
    @allure.title('用户能正常登录')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1','--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order = 1)     # 让登录用例默认第一步执行
    def test_login(self):
        '''
        用户登录的测试用例
        :return:
        '''
        self.login_object = Api_Login()
        resp_login = self.login_object.login_success()
        # print(resp_login)
        # assert resp_login.get('ok') == True
        assert resp_login['ok'] == True             # 响应信息为字典时，断言可以用 get('ok'),也可以用 ['ok']


# if __name__ == '__main__':
# #     # TestLogin().test_login()
#     pytest.main(["-sv"])