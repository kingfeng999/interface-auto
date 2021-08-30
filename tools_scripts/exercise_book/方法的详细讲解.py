# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/13 1:33 上午
# @Author: zhifeng.qin
# @File: 方法的详细讲解.py
# @Software: PyCharm

class Dog():

    # 定义私有类属性
    __tooth = 100

    # 定义一个魔法方法
    def __init__(self, name):
        self.name = name

    # 定义一个类方法，类方法配合类属性调用
    @classmethod
    def get_tooth(cls):
        print(cls.__tooth)

    # 定义一个静态方法，只返回固定一条数据，不需要调用属性的场景使用静态方法
    @staticmethod
    def info():
        print('聪明的狗狗跑得很快')

    # 定义一个实例方法，实例方法配合实例属性使用
    def play(self):
        print(f'我家有一条聪明的狗狗，它的名字叫：{self.name}')

# 构建类实例对象进行调用
dog = Dog('xiaohei')
dog.play()
dog.info()
dog.get_tooth()



