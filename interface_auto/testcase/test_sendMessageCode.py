#!/usr/bin/python3
# @Time: 2021/4/1 17:16
# @Author: qinzhifeng
# @File: test_sendMessageCode.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiSendMessageCode import Api_send_message_code

class TestSendMessageCode():

    @allure.feature('支付验证码发送功能')
    @allure.story('正常发送场景')
    @allure.title('用户能正常接收验证码')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order=4)
    def test_send_message_code(self):
        self.code = Api_send_message_code()
        resp_code = self.code.send_message_code()

        # 对请求结果进行断言
        assert resp_code['ok'] == True
