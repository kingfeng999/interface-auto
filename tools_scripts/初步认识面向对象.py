# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/18 23:40 下午
# @Author: zhifeng.qin
# @File: 初步认识面向对象.py
# @Software: PyCharm

'''
    自动化班面向对象的基本使用演示案例
'''

class Plane():

    def __init__(self, name, color):
        '''
        初始化方法，init 中定义的属性叫实例属性
        :param name: 飞机的名字
        :param color: 飞机的颜色
        '''
        self.name = name
        self.color =color

    def fly(self):
        print(f'飞机的名字是：{self.name}，颜色是：{self.color}，它可以飞得很高')

    def shoot(self):
        print('飞机还可以射击')

    def __str__(self):
        return '这只是一个飞机的图纸'

p = Plane('阿帕奇', '绿色')
p.fly()
p.shoot()
print(p.__str__())







