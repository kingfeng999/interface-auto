# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/27 7:57 下午
# @Author: zhifeng.qin
# @File: conftest.py
# @Software: PyCharm
'''
conftest.py名字是固定的(本文件主要是用来解决中文不显示问题)
钩子函数(hook)--名字是固定
pytest_collection_modifyitems(items)(重点是知道运行时机什么样子)，items 指的是收集的测试用例
底层对用例名字起作用的两个字段 name,_nodeid
unicode_escape（按此方式解码为中文）
'''
def pytest_collection_modifyitems(items):

    # print('测试')
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')             # encode() 是编码，decode()是解码
        item._nodeid = item.nodeid.encode().decode('unicode_escape')


