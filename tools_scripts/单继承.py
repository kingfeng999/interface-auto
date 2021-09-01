# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/12 4:13 ??
# @Author: zhifeng.qin
# @File: 单继承.py
# @Software: PyCharm


# 最基础，不带 init ，不需要重写方法的继承（单继承）
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

class B(A):
    def run(self):
        print(888)

son = B()
print(son)
print(son.num)
print(son.info_print())


# 带 init 方法，需要重写父类同名方法的继承（单继承）
# 父类
class Parent(object):
    def __init__(self, name):
        self.name = name

# 儿子类
class Son(Parent):
    def __init__(self, name, age):
        self.age = age          # 重写拥有年龄的属性（可理解为新增）
        super().__init__(name)    # 继承保留原来的 name 属性，可以用 super 方法

# 孙子类
class Grandson(Son):
    def __init__(self, name, age, gender):
        self.gender = gender
        # super().__init__(name, age)

        # 继承除了用 super，还可以通过类来调用同名方法实现
        Son.__init__(self, name, age)


# 调用类，打印一些信息
gs = Grandson('Grandson', 12, '男')
print(f'姓名： {gs.name}')
print(f'年龄： {gs.age}')
print(f'性别： {gs.gender}')







