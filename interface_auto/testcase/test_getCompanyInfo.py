#!/usr/bin/python3
# @Time: 2021/4/1 22:04
# @Author: qinzhifeng
# @File: test_getCompanyInfo.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiGetCompanyInfo import Api_get_company_info


class TestGetCompanyInfo():

    @allure.feature('获取公司信息功能')
    @allure.story('获取公司信息验证场景')
    @allure.title('用户能正常获取公司信息')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order = 7)
    def test_get_company_info(self):
        '''
            获取公司信息测试用例
        :return:
        '''
        self.company_info = Api_get_company_info()
        resp_message = self.company_info.get_company_info()

        # 对请求结果进行断言
        assert resp_message['ok'] == True

