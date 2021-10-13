#!/usr/bin/python3
# @Time: 2021/2/4 16:27
# @Author: qinzhifeng
# @File: run_testcase.py
# @Software: PyCharm

import pytest
import subprocess

'''
此文件为运行 pytest 测试用例的脚本

================ 原 pytest.ini 文件写法 ==================
[pytest]
addopts = -sv --alluredir ./reports/ringle --clean-alluredir
testpaths = ./testcase
python_files = test_*.py
python_classes = Test*
python_function = test_*
log_cli = 1        指的是：可以同时在 Terminal 终端下打印日志！

脚本运行：		pytest -sv ./testcase/test_login.py --alluredir ./reports/ringle
allure 启动：	allure generate ./reports/ringle -o ./reports/ring_rep --clean

'''


# if __name__ == '__main__':
#     # pytest 运行测试用例的命令
#     pytest.main(['-sv', './testcase/', '--alluredir=./reports/ringle', '--clean-alluredir'])
#
#     # subprocess: 把在终端操作的命令行转移到 python 文件中操作,shell=True 接收这个命令，并以 shell 脚本的形式运行
#     subprocess.call('allure generate ./reports/ringle -o ./reports/ringle_html/ --clean', shell = True)
#
    
    
    
    