#!/usr/bin/python3
# @Time: 2021/2/4 21:22
# @Author: qinzhifeng
# @File: test_logout.py
# @Software: PyCharm

from interface_auto.base_api.apiLogout import ApiLogout
import allure
from interface_auto.tools.logger import GetLogger
import pytest

logger =GetLogger().get_logger()

class TestLogout():

    @allure.feature('退出功能')
    @allure.story('正常退出场景')
    @allure.title('用户能正常退出登录')
    @allure.severity('Critical')
    @allure.issue('https://pms.kouling.cn/index.php?m=bug&f=browse&productID=1', '--> 如果执行失败，这里可以提交 Bug 到禅道')
    @pytest.mark.last           # 可以使退出登录用例最后一个执行
    def test_logout(self):
        '''
        用户退出登录的测试用例
        :return:
        '''
        self.logout_obj = ApiLogout()
        logout = self.logout_obj.logout_success()
        # logout = logout.json()
        logger.info('登录接口返回数据类型是：{}'.format(type(logout)))
        logger.info('登录接口返回数据是：{}'.format(logout))
        assert logout['ok'] == True



# if __name__ == '__main__':
#     TestLogout().test_logout()