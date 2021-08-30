#!/usr/bin/python3
# @Time: 2021/2/4 14:18
# @Author: qinzhifeng
# @File: logger.py
# @Software: PyCharm

import logging.handlers
from interface_auto.config import DIR_NAME

'''
    日志 logging
    作用:    类似print,调试的，便于排查问题(查看报错信息)
    加日志:    便于排查问题，在那个位置加日志
    
    步骤：
    1.日志器  启动日志的入口
    级别： 原则：你设置的级别，比他大的都会显示出来，比他低级的级别是不会显示出来，级别从低到高
    debug(调试级别)  
    info(信息级别)  
    warning(警告级别) 
    error(错误级别)  
    critical(致命的，严重的)
    
    2.格式器  要以什么样的格式展现日志
    3.处理器   表示你对日志内容的一个处理方式，放在文件里面保存还是直接输入到console里面
'''

## 单例模式的思想：通过逻辑控制，只生成一个对象
class GetLogger:
    '''
    当已经创建了logger对象的时候，那么之后就不在创建了，也就是只创建一次对象
    '''
    # 把logger对象的初始值设置为None
    logger = None

    # 创建logger，并且返回这个logger
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            ########创建日志器，控制他的创建次数
            cls.logger = logging.getLogger()  # 不是None
            # 设置总的级别
            cls.logger.setLevel(logging.INFO)
            # 2获取格式器
            # 2.1 要给格式器设置要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 2.2创建格式器，并且给他设置样式
            fm = logging.Formatter(fmt)
            # 3.创建处理器 按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename= DIR_NAME +'/logger/ringle.log',  # 原日志文件
                                                           when='H',  # 间隔多长时间把日志存放到新的文件中
                                                           interval=1,
                                                           backupCount=3,  # 除了原日志文件，还有3个备份
                                                           encoding='utf-8'
                                                           )

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)

            # return cls.logger
        return cls.logger



if __name__ == '__main__':
    logger = GetLogger().get_logger()
    # print(id(logger))
    # logger1 = GetLogger().get_logger()
    # print(id(logger1))
    # logger.debug('调试')  # 相当print小括号中的信息
    # logger.info('信息')
    # logger.warning('警告')
    # name = 'yaoyao'
    # logger.error('这个变量是{}'.format(name))
    # logger.critical('致命的')
