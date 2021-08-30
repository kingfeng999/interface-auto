#!/usr/bin/python3
# @Time: 2021/4/1 21:17
# @Author: qinzhifeng
# @File: test_payStatus.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiPayStatus import Api_pay_status


class TestPayStatus():

    @allure.feature('查询支付状态功能')
    @allure.story('查询支付验证码场景')
    @allure.title('用户支付验证码状态正确')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order = 6)
    def test_pay_status(self):
        '''
            查询支付状态测试用例
        :return:
        '''
        self.status = Api_pay_status()
        resp_status = self.status.pay_status()

        # 对请求结果进行断言
        assert resp_status['ok'] == True



