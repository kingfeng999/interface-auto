#!/usr/bin/python3
# @Time: 2020/12/21 15:00
# @Author: qinzhifeng
# @File: managing_pages.py
# @Software: PyCharm

from exercise_book.base_setting import Base_login
from appium import webdriver
import time

'''
登录成功以后，页面遍历操作10分钟左右
'''


# 用户操作
def __init__(self, driver):
    self.driver = driver
    # 调用登录数据
    Base_login()
    time.sleep(2)
    print(20 * "-*" + " 如下是用户操作 app 的记录：" + 20 * "-*")


def caozuo(self):
    # for i in range(0, 5):
    # 第一个动作：找人页发布个人需求
    self.driver.find_element_by_id('com.ringleai.ai:id/tv_hint').send_keys('测试')
    el = self.driver.find_element_by_id('com.ringleai.ai:id/rlBtnRecommend')
    if el is not None:
        print("存在一键推送按钮")
    else:
        print("该元素找不到")
    self.driver.find_element_by_id('com.ringleai.ai:id/ib_back')

    # 第二个动作：机会页点击我要应聘发送5条消息，返回到机会页后点击技能列表，再次返回机会页

    # 第三个动作：点击消息页，点击联系人按钮，返回消息页

    # 第四个动作，遍历点击我的订单、虚拟公司、余额、我的技能、我的企业、我的简历，返回页面后点击虚拟公司开启直播，直播时长2分钟左右


if __name__ == '__main__':
    # man = managing()
    caozuo()
