# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/2/1 11:41 上午
# @Author: zhifeng.qin
# @File: setting.py
# @Software: PyCharm

'''
    1、存放公共配置文件（IP,端口号）
    2、上下游接口关联的数据
    3、以常量的方式进行编写        变量（大写） = 值
'''

import os
IP = 'http://121.42.15.146:9090/'
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}

# 动态生成绝对路径
ABS_PATH = os.path.abspath(__file__)        # 返回当前文件绝对路径
DIR_NAME = os.path.dirname(ABS_PATH)        # 最终返回文件夹路径


# 如果是动态产生的数据 我们直接导入文件，然后用文件.变量去使用
JUMP_URL = None
