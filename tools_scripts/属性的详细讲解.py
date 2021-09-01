# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/12 10:08 下午
# @Author: zhifeng.qin
# @File: 属性的详细讲解.py
# @Software: PyCharm

class Dog(object):
    tooth = 10          # 这是类属性，实例对象和类都可以调用
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
print(f"通过类访问类属性，狗有{Dog.tooth}颗牙齿！")
print("通过实例对象访问类属性，小黑有{}颗牙齿！".format(xiaohei.tooth))

Dog.tooth = 20      # 只有类才可以修改类属性
print(f'只有类才可以修改类属性，修改后的类属性值为：{Dog.tooth}')

'''
    实例对象修改实例属性，只能通过实例对象访问实例属性
'''
print("只能通过实例对象访问实例属性，小黑的年龄是：{}岁".format(xiaohei.age))
print(f"只能通过实例对象访问实例属性，旺财的年龄是：{wangcai.age}岁")

# 实例对象修改实例属性
xiaohei.age = 1001
wangcai.age = 2001
print(f"修改年龄后，小黑是{xiaohei.age}岁")
print(f"修改年龄后，旺财是{wangcai.age}岁")


# 以下写法会报错，不能通过类对象访问实例属性
# print(Dog.age)












