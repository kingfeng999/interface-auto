#!/usr/bin/python3
# @Time: 2020/12/21 16:23
# @Author: qinzhifeng
# @File: 999.py
# @Software: PyCharm

import os

# print(os.path.dirname(__file__))          # 返回文件目录路径，__file__ 指的是当前文件
# base_path = os.path.dirname(__file__)

# # 把生成的报告放到reports目录下
# print(os.path.join(base_path, 'reports', 'demo.txt'))     # 将目录和文件名合成一个路径
# print(os.path.join(base_path, 'demo.txt'))     # 将目录和文件名合成一个路径（支持任意个数）
# print(os.path.abspath(__file__))                            # 输出绝对路径


# 动态生成绝对路径(最推荐使用)
# base_path = os.path.dirname(__file__)
# file = os.path.join(base_path, 'reports','demo.txt')
# print(file)
# with open(file, 'a') as f:
#     f.write('\ntest\nhaha')


# 创建一个飞机类
# class Plane(object):
#     # 方法
#     def fly(self):
#         print('飞机可以飞')
#
# # 创建对象  对象=类名（）
# redPlane = Plane()
#
# # 方法的调用： 对象.方法（）进行调用
# redPlane.fly()


'''
摆放家具的案例

抽离两个类
1.房子
属性
方法

2.家具
属性
方法
'''

# 定义家具类
class HouseItem:

    # 定义实例属性
    def __init__(self,name,area):
        self.name = name    # 家具的名称
        self.area = area    # 家具占地面积
    # 方法
    def __str__(self):
        return f'家具名字{self.name},家具占地面积{self.area}'


# 定义房子类
class House:
    # 定义属性
    def __init__(self,house_type,house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.items_list = []            # 家具列表
        self.free_area = house_area

    def add_item(self, item):
        '''
        添加家具的方法
        :param item: 家具  对家具类进行一个实例化
        家具类所定义的所有的属性，我们这个家具item 都是同样具有的
        :return:
        '''
        # 剩余面积 < 家具面积
        if self.free_area < item.area:  # 家具的面积  item.area
            print('房子太小了，家具放不下了')
        else:
            # 正常往房间里面放家具'
            self.items_list.append(item.name)  # 添加家具的名字 item.name
            # 剩余面积 = 剩余面积-家具面积
            self.free_area -= item.area

    def __str__(self):
        return  f'户型{self.house_type},总面积:{self.house_area},剩余面积{self.free_area}'


if __name__ == '__main__':
    # 实例化一个家具对象   对象=类()
    bed = HouseItem('席梦思', 4)
    chest =HouseItem('衣柜',2)
    table = HouseItem('桌子',1.5)
    print(bed)

    # 创建房子的对象   房子对象=房子类()
    house =House('三室二厅',100)
    #  # 往房间里面放家具
    print('没有放家具之前的house{}'.format(house))
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print('放家具之后的house{}'.format(house))

    # 在类的外面定义属性color
    bed.color = '红色'
    print(bed.color)



