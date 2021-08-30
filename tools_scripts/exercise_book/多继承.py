# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/18 23:43 下午
# @Author: zhifeng.qin
# @File: 多继承.py
# @Software: PyCharm

'''
    自动化班多继承演示案例：子类有多个父类场景的多继承用法
'''
class Human(object):
    def __init__(self, sex):
        self.sex = sex

    def p(self):
        print('这是 Human 的方法')

class Person:
    def __init__(self, name):
        self.name = name

    def p(self):
        print('这是 Person 的方法')

    def person(self):
        print('这是 person 特有的方法')


# 单继承,继承 Person 类
class Teacher(Person):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)      # 通过 super()方法继承

'''
    多继承演示，当使用多继承时，继承父类的属性最好不用 super() 方法，小问题比较多，建议用：父类名.同名方法的方式继承
'''
class Student(Human, Person):
    def __init__(self, name, sex, grade):
        # 通过父类名.同名方法的方式继承父类
        Person.__init__(self, name)
        Human.__init__(self, sex)

        self.grade = grade

    def p(self):
        print('-------')

class Son(Human, Teacher):
    def __init__(self, sex, name, age, fan ):
        Human.__init__(self, sex)
        Teacher.__init__(self, name, age)

        self.fan = fan

# 创建对象调用
stu = Student('张三', '男', 88)
print(stu.name, stu.sex, stu.grade)
stu.p()    # 父类 Human 和 Person 都有同名 p 方法，这里会先调用 Human 中的 P 方法，按继承顺序








