#!/usr/bin/python3
# @Time: 2021/4/2 17:12
# @Author: qinzhifeng
# @File: test_addJob.py
# @Software: PyCharm

import allure
import pytest
from interface_auto.base_api.apiAddJob import Api_add_job
from interface_auto.tools.logger import GetLogger

logger = GetLogger().get_logger()

class TestAddJob():

    @allure.feature('发布岗位信息功能')
    @allure.story('发布标准极速岗场景')
    @allure.title('能正常发布标准极速岗位')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.run(order = 8)
    def test_add_two_job(self):
        '''
            发布标准极速版简历
        :return:
        '''

        self.two_job = Api_add_job()
        resp_job = self.two_job.add_two_type_job()

        # 对结果进行断言
        assert resp_job['ok'] == True



