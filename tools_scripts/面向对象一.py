#!/usr/bin/python3
# @Time: 2021/1/6 15:37
# @Author: qinzhifeng
# @File: 面向对象一.py
# @Software: PyCharm

'''
    定义家具类
    定义房子类
'''

# 定义家具类
class HouseItem():

    # 定义魔法方法
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名字是：{self.name}，家具占地面积是：{self.area}平方米'


# 定义房子类
class House():

    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.item_list = []
        self.free_area = house_area

    # 定义房子添加家具的方法
    def add_item(self, item):
        '''
            给房子添加家具
        :param item: item 是家具名字
        :return:
        '''

        # 添加家具，判断房子的面积，item.area 是家具的占地面积
        if self.free_area < item.area:
            print('房子太小了，家具放不下')
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area

    def __str__(self):
        return f'房子类型是：{self.house_type}, 房子面积是：{self.house_area}平方米, 添加家具后剩余面积是：{self.free_area}平方米'



if __name__ == '__main__':
    shafa = HouseItem('沙发',30)
    bed = HouseItem('床', 20)
    table = HouseItem('桌子', 13)
    print(shafa,'\n',bed, '\n', table)

    house = House('八房三厅', 800)
    house.add_item(shafa)
    house.add_item(bed)
    house.add_item(table)
    print(house)

