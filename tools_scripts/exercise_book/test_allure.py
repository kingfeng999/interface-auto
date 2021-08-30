# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/28 3:39 下午
# @Author: zhifeng.qin
# @File: test_allure.py
# @Software: PyCharm

'''
1.环境配置
allure：
前提：java环境，jdk
1.allure-pytest  pip install allure-pytest
2.allure服务  文件夹  配置环境变量
文档有写
2.以装饰器的形式去用
掌握：allure装饰器对应的在allure报告中对应的样式
@装饰器
@装饰器
@....
def 测试用例

3.
如何生成allure报告
3.1  启动pytest执行的命令:  --alluredir   报告保存的路径
3.2  启动allure服务

4.三大标记
@allure.feature(str)：主要功能
@allure.story(str)： 子功能
@allure.severity()
1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：临界缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）

@allure.step() 在报告中添加步骤
@allure.title()  给测试用例起名字
对用例进行详细的描述(函数文档)
1. 函数文档的书写方式
2. @allure.description(str)
3. @allure.description_html('html的内容')

关于链接，点击进去可以跳转到对应的链接地址
@allure.link(url)
@allure.testcase(url)
@allure.issue(url)
区别:样式不一样
一样：本质一样，后面两个的方法其实都是调用的@allure.link()

allure.attach(body,name,type) 不需要装饰器的使用
场景: 可以在报告中添加附件 png,jpg,pdf
body:要显示的内容
name:自定义的内容的名字
type:附件类型

'''

# 写登录的步骤
import allure


@allure.step('1.输入用户名')
def input_username():
    pass

@allure.step('2.输入密码')
def input_password():
    pass

@allure.step('3.点击登录')
def click_login():
    pass

def login():
    input_username()
    input_password()
    click_login()

@allure.link('https://www.baidu.com/')
@allure.feature('用户功能')
@allure.story('登录功能的测试用例')
@allure.severity('blocker')
@allure.title('登录的测试用例')
def test_login():
    '''
    对登录功能步骤的详细描述，然后进行断言
    :return:
    '''
    login()
    # 1.读取文件的内容
    with open('./demon1.jpg','rb') as f:
        # 要显示的文件的内容
        content = f.read()
    allure.attach(content,'上传了一张图片',allure.attachment_type.JPG)

    assert 1 == 1

@allure.issue('http://121.42.15.146:9090/mtx/','bug管理平台的链接地址')
@allure.description('对注册功能的测试用例的描述，并对那个字段进行断言')
@allure.feature('用户功能')
@allure.story('注册的测试用例')
@allure.severity('critical')
@allure.title('注册的测试用例')
def test_register():

    assert 1==1

@allure.testcase('http://121.42.15.146:9090/mtx/')
@allure.description_html('<h1>下单的测试用例</h1>')
@allure.title('下订单的测试用例')
def test_order():
    assert 1==1
