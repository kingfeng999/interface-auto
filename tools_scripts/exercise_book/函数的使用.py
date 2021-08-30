# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/14 4:08 下午
# @Author: zhifeng.qin
# @File: 函数的使用.py
# @Software: PyCharm


# def sum(a, b):
#     result = a * b
#     # print(result)
#     return result
#
# sum = sum(5,8)
# print(sum)
# sum(6,9)
#
def test1():
    print(11111)

def test2():
    print('start2')
    print(22222)
    print('start1')
    test1()

test2()

# 常规函数
def fn1():
    return 200

print(fn1())

# 如果一个函数只有一个返回值，并且只有一句代码时可以使用匿名函数，语法： lambda 参数：表达式（参数可省略）
fn2 = lambda:20000
print(fn2())

# 使用匿名函数进行计算
a = 2
b = 3
fn3 = lambda : a+b
print(f'使用匿名函数计算结果是：{fn3()}')

# 计算列表中每个元素都乘以2，交打印出值
list0 = [10,20,30]
list1 = []
for i in list0:
    i *= 2
    list1.append(i)
print(list1)


# 高阶函数 map 的使用
# map()函数，会根据提供的函数对指定序列做映射，语法为：map(函数名，一个或多个序列)，返回值，python3 返回的是迭代器
# 结合 lambda 函数，通过 map 函数计算列表中每个元素都+2
list5 = [10,20,30,40]
result = map(lambda x:x+2, list5)
print(result)
new_list = list(result)     # 返回的结果是迭代器，想要得到列表，需要通过 list()方法进行转换
print(new_list)


# 单独使用 map 并结合普通函数实现列表元素都+2
list7 = [100,200,300]
def s(x):
    return x + 2
l = map(s, list7)
l1 = list(l)
print(l1)


# 高阶函数 filter()使用，语法：filter(函数名，序列名)
# 需求：将列表中的偶数筛选出来
num = [2,5,8,9,10,11,12,15,17,19,22,2]
def aa(x):
    if x % 2 == 0:
        return x
bb = filter(aa, num)
print(list(bb))


# 高阶函数 reduce()使用，语法：reduce(函数名（x,y）, lst)，该函数会对参数序列中元素进行累积，需要导包：from functools import reduce
# 其中函数名必须有两个参数，每次计算的结果继续和下一个元素做累积计算
from functools import reduce
cc = [1,2,3,4,5]
def dd(x,y):
    x = x + y
    return x
result = reduce(dd, cc)
# 用 lambda 函数写法
# result = reduce(lambda x,y : x + y , cc)
print(result)


# 普通方法计算元素的和
aaa = [1,2,3,4,5]
sum = 0
for i in aaa:
    sum += i
print(sum)


sum = 0
for i in range(101):
    sum += i
print(sum)











