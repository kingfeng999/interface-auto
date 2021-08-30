#!/usr/bin/python3
# @Time: 2020/12/10 16:48
# @Author: qinzhifeng
# @File: base_setting.py
# @Software: PyCharm

from appium import webdriver
import time

'''
耗电量自动化操作脚本
设置页面登录准备数据
'''


class config:

    def __init__(self, driver):
       self.driver = driver


    def start(self):
        '''
        app 启动项配置
        :return:
        '''
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "10.0",
            "deviceName": "CUY0219527002353",
            "appPackage": "com.ringleai.ai",
            "appActivity": "com.ringleai.ringle.ui.launch.LaunchActivity",
            "autoGrantPermisions": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            'automationName': 'UiAutomator2'
        }

        # 创建 driver
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

        driver.implicitly_wait(20)

        # 用户登录授权
        driver.find_element_by_id(
            "com.ringleai.ai:id/rlAlertPositiveBtn").click()  # 同意获取用户协议及隐私声明
        driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_always_button").click()  # 同意获取设备位置信息
        driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_button").click()  # 允许访问设备上的相片
        driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_button").click()  # 允许 app 获取设备信息

        # 通过手机号登录
        driver.find_element_by_id("com.ringleai.ai:id/rlLoginByMobile").click()
        driver.find_element_by_id("com.ringleai.ai:id/rlMobileEt").send_keys("12584566888")
        driver.find_element_by_id("com.ringleai.ai:id/rlSmsCodeEt").send_keys("112334")
        driver.find_element_by_id("com.ringleai.ai:id/rlNext").click()
        print("用户登录成功")
        time.sleep(3)
        return driver


    def caozuo(self):
        print(20 * "-*" + " 如下是用户操作 app 的记录：" + 20 * "-*")
        # 第一个动作：找人页发布个人需求
        self.driver.find_element_by_id("com.ringleai.ai:id/tv_hint").click()
        self.driver.find_element_by_id("com.ringleai.ai:id/rlEdit").send_keys("测试")
        el = self.driver.find_element_by_id('com.ringleai.ai:id/rlBtnRecommend')
        if el is not None:
            print("存在一键推送按钮")
        else:
            print("该元素找不到")
        self.driver.find_element_by_id('com.ringleai.ai:id/ib_back')


if __name__ == '__main__':
    con = config(driver = webdriver)
    con.start()
    con.caozuo()
