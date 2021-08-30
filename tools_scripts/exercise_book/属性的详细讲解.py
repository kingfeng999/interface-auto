# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/12 10:08 下午
# @Author: zhifeng.qin
# @File: 属性的详细讲解.py
# @Software: PyCharm

class Dog(object):
    tooth = 10          # 这是类属性
    def __init__(self):
        self.age = 5            # age 是实例属性

    def info_print(self):       # 定义实例方法
        print(self.age)

# 创建对象调用
xiaohei = Dog()
wangcai = Dog()

'''
    类属性的访问和修改
'''
# 类和对象都可以访问类属性
print(Dog.tooth)
print(xiaohei.tooth)

Dog.tooth = 20      # 只有类才可以修改类属性
print(f'修改后的类属性值为：{Dog.tooth}')

'''
    实例属性的访问和修改，只能通过实例对象访问实例属性
'''
# xiaohei.age = 1001
# Dog.age = 2000
print(xiaohei.age)
print(Dog.age)     # 会报错，不能通过类对象访问实例属性
print(wangcai.age)











