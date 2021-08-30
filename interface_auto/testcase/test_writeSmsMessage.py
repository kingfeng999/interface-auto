#!/usr/bin/python3
# @Time: 2021/4/1 18:02
# @Author: qinzhifeng
# @File: test_writeSmsMessage.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiWriteSmsMessage import Api_write_sms_message
import time


class TestWriteSmeMessage():

    @allure.feature('支付验证码验证功能')
    @allure.story('支付验证码验证场景')
    @allure.title('用户能输入验证码验证正确')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    # @pytest.mark.run(order=5)
    def test_write_sms_message(self):
        self.write_message = Api_write_sms_message()
        resp_message = self.write_message.write_sms_message()

        # 对请求结果进行断言
        assert resp_message['ok'] == True

        time.sleep(0.5)
