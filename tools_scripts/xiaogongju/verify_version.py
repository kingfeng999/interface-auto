#!/usr/bin/python3
# @Time: 2020/12/31 22:56
# @Author: qinzhifeng
# @File: verify_version.py
# @Software: PyCharm

from ftplib import FTP
import re
import os
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
'''
需求：渠道包自动化验证工具
背景：android 上线以后渠道包有几十个，手工验证冒烟流程和渠道号对比，效率慢
目的：通过自动化手段解决人工验证耗时长的问题
    实现逻辑：
    1、先从 FTP 下载安装包到电脑本地
    2、再从电脑本地获取安装包，安装到手机上
    3、安装成功后自动跑冒烟流程，自动对比渠道号
    4、手机上自动卸载 app 再安装新的渠道包进行验证
    5、验证结果通过日志打印保存到相关文件中
'''
def ftpapk():
    '''
    将 FTP 上的安装包导入本地
    否则异常会影响到源包
    '''
    ftp = FTP()
    ftp.connect('172.10.20.153', 21)
    ftp.login('', '')
    ftp.encoding = 'gbk'
    ftp.cwd("ftp-android/RingleAi/ringle-android/outputs/V2.12.0")     # FTP下载地址
    apk = ftp.nlst()
    for i in apk:
        print(i)
        bufsize = 1024
        fp = open(r'E:/渠道包/'+i, 'wb').write                        # 本地地址
        print("正在下载",i,"安装包")
        res = ftp.retrbinary('RETR ' + i,fp,bufsize)
    message = "下载完成，请检查本地文件"
    return message

def channel():
    '''
    渠道包验证
    '''
    channelpath = os.listdir("E:\渠道包")
    with open(r'C:\Users\EDZ\Desktop\灵鸽渠道号.txt','rb') as f:
        qapk = f.read().decode("utf-8")
        sapk = re.split(r"\s|\r|\n|' '",qapk)
        mapk = []       # 新建空列表，去掉空格和 channel
        zapk = []       # 新建空列表，放渠道名称
        oapk = []       # 新建空列表，放渠道号
        tapk = {}

        # 去掉空格和 channel，新数据放到 mapk[] 列表
        for k in sapk:
            if k != 'channel' and k != '':
                mapk.append(k)
        s = 0

        # 通过列表元素下标0，1区分渠道名称和渠道号
        for p in range(len(mapk)):
            if (p % 2) == 0:
                # 添加到渠道号名称列表
                zapk.append(mapk[p])
            else:
                # 添加到渠道号列表
                oapk.append(mapk[p])
        aaop = dict(zip(zapk,oapk))          # 放到一个新字典

        for key in aaop.keys():                   # 要验证的渠道包
            for apk in channelpath:               # 本地文件路径
                # print(key,oksod)
                if key in apk:
                    print("寻找",key,"安装包，已找到",apk,"安装包")
                    akpath = os.path.join(r'E:\渠道包',apk)
                    desired_caps = {
                        "platformName": "Android",
                        "platformVersion": "10",
                        "deviceName": "GPG4C19125006264",
                        "app": akpath,
                        "appPackage": "com.ringleai.ai",
                        "appActivity": "com.ringleai.ringle.ui.launch.LaunchActivity",
                    }
                    print("正在安装中。。。")
                    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                    print("安装完成。。。")
                    print("需要校验的channel为:", aaop[key])
                    driver.find_element_by_id("com.ringleai.ai:id/rlAlertPositiveBtn").click()  # 点击同意
                    driver.implicitly_wait(10)
                    driver.find_element_by_id(
                        "com.android.permissioncontroller:id/permission_allow_always_button").click()  # 点击始终允许
                    driver.implicitly_wait(10)
                    driver.find_element_by_id(
                        "com.android.permissioncontroller:id/permission_deny_button").click()  # 点击始终允许
                    driver.find_element_by_id(
                        "com.android.permissioncontroller:id/permission_deny_button").click()  # 点击始终允许
                    driver.implicitly_wait(10)
                    driver.tap([(936, 2211), (72, 72)], 100)  # Vsimka
                    driver.implicitly_wait(10)
                    driver.tap([(158, 1200), (923, 1335)], 100)  # 点击插入
                    driver.implicitly_wait(10)
                    driver.tap([(30, 1974), (1050, 2118)], 100)  # 点击相册
                    driver.implicitly_wait(10)
                    driver.tap([(96, 1794), (984, 1926)], 100)  # 点击允许
                    driver.implicitly_wait(10)
                    driver.tap([(208, 258), (352, 402)], 100)  # 选择图片
                    driver.implicitly_wait(10)
                    driver.tap([(816, 2149), (1080, 2208)], 100)  # 选择完成
                    driver.implicitly_wait(10)
                    driver.find_element_by_id("com.ringleai.ai:id/rlPasswordEdt").send_keys('sugber999')
                    driver.implicitly_wait(10)
                    driver.find_element_by_id("com.ringleai.ai:id/rlLogin").click()
                    sleep(10)
                    driver.tap([(876, 2158), (1014, 2208)], 100)

                    def getSize():  # 获取当前的 width 和 height 的x、y的值
                        x = driver.get_window_size()['width']  # width为x坐标
                        y = driver.get_window_size()['height']  # height为y坐标
                        return (x, y)

                    def swipeUp(t):  # 当前向上滑动swipeup
                        l = getSize()
                        x1 = int(l[0] * 0.5)
                        y1 = int(l[1] * 0.75)
                        y2 = int(l[1] * 0.25)
                        driver.swipe(x1, y1, x1, y2, 500)  # 设置时间为500

                    swipeUp(9000)
                    swipeUp(9000)

                    driver.implicitly_wait(10)
                    driver.tap([(72, 2059), (390, 73)], 100)  # 进入关于手机
                    driver.implicitly_wait(10)
                    asx = driver.find_element_by_id('com.ringleai.ai:id/rlLogo')  # 获取logo的id
                    TouchAction(driver).long_press(asx).perform()  # 长按
                    sleep(1)
                    mms = driver.find_element_by_id("com.ringleai.ai:id/rlAlertMsg")  # 数据读取
                    asd = re.findall(r"Channel:(.+?)\n", mms.text)
                    driver.remove_app("com.ringleai.ai")        # 将 app 卸载掉

                    # app 上显示的渠道号与本地渠道号进行对比
                    for pop in asd:
                        print("安装包channel为:",pop)
                        if pop == aaop[key]:
                            print("验证通过")
                        else:
                            print("验证不通过")


if __name__ == '__main__':
    # a = ftpapk()
    b = channel()