#!/usr/bin/python3
# @Time: 2021/4/1 15:57
# @Author: qinzhifeng
# @File: test_unionPayCard.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiUnionPayCard import Api_union_pay_card

class TestUnionPayCard():

    @allure.feature('银联卡充值功能')
    @allure.story('正常充值场景')
    @allure.title('用户能正常充值')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order=3)
    def test_union_pay_card(self):

        self.pay = Api_union_pay_card()
        resp_pay = self.pay.union_pay_card()

        # 对请求结果进行断言
        assert resp_pay['ok'] == True
