#!/usr/bin/python3
# @Time: 2021/4/1 14:53
# @Author: qinzhifeng
# @File: test_getbanklist.py
# @Software: PyCharm

import allure
from interface_auto.base_api.apiGetBankList import Api_get_bank_list
import pytest

class TestGetBankList():

    @allure.feature('获取银行卡列表功能')
    @allure.story('正常获取场景')
    @allure.title('用户能正常获取')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order = 2)
    def test_get_bank_list_success(self):
        '''
            正常获取银行卡列表的测试用例
        :return:
        '''

        self.back_list = Api_get_bank_list()
        resp_back_list = self.back_list.get_bank_list()

        # 对请求结果进行断言
        # assert resp_login.get('ok') == True
        assert resp_back_list['ok'] == True         # 响应信息为字典时，断言可以用 get('ok'),也可以用 ['ok']