# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/12 8:19 下午
# @Author: zhifeng.qin
# @File: 多态.py
# @Software: PyCharm

'''
    多态的详细讲解
实现步骤：
1、定义父类，并提供公共方法
2、定义子类，并重写父类方法
3、传递子类对象给调用者，可以看到不同子类执行效果不同
'''

# 狗为父类
class Dog():
    text = '喜欢溜达'
    def play(self):
        print(self.text)

class LilyDog(Dog):
    text = '喜欢在商城溜达'

class TomDog(Dog):
    text = '喜欢在公园溜达'

class Pet():
    def play_with_dog(self, dog):
        dog.play()

lily = LilyDog()
tomdog = TomDog()
var = Pet()
var.play_with_dog(lily)
var.play_with_dog(tomdog)






