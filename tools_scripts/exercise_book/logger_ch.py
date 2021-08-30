# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/29 2:52 下午
# @Author: zhifeng.qin
# @File: logger_ch.py
# @Software: PyCharm

'''
日志 logging
作用:类似print,调试的，便于排查问题(查看报错信息)
加日志:便于排查问题，在那个位置加日志
1.日志器  启动日志的入口
级别： 原则：你设置的级别，比他大的都会显示出来，比他低级的级别是不会显示出来的
级别从低到高
debug(调试级别)  info(信息级别)  warning(警告级别) error(错误级别)  critical(致命的，严重的)
2.格式器  要以什么样的格式展现日志
3.处理器   表示你对日志内容的一个处理方式，放在文件里面保存还是直接输入到console里面
'''

# 导包 把日志模块和处理器一并导入
import logging.handlers

# 1.获取日志器(日记本)
logger = logging.getLogger()

# 设置总的级别
logger.setLevel(logging.ERROR)

# 2获取格式器
# 2.1 要给格式器设置要输出的样式
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
fm=logging.Formatter(fmt)       # 2.2创建格式器，并且给他设置样式

# 3.创建处理器 按照时间进行切割文件
tf =logging.handlers.TimedRotatingFileHandler(filename='./test.log', # 原日志文件
                                          when='S',  # 间隔多长时间把日志存放到新的文件中
                                          interval=1,
                                          backupCount=3, # 除了原日志文件，还有3个备份
                                          encoding='utf-8'
                                          )
# 在处理器中添加格式器
tf.setFormatter(fm)

# 在日志器中添加处理器
logger.addHandler(tf)


if __name__ == '__main__':
    # 调试的调用过程

    logger.debug('调试')  # 相当print小括号中的信息
    logger.info('信息')
    logger.warning('警告')
    name = 'yaoyao'
    logger.error('这个变量是{}'.format(name))
    logger.critical('致命的')









