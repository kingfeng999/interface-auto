#!/usr/bin/python3
# @Time: 2021/5/8 14:24
# @Author: qinzhifeng
# @File: identity.py
# @Software: PyCharm

'''
    生成有效的身份证号
'''

import random
import re
# 导入某个模块的部分类或方法
from datetime import datetime, timedelta

# 导入常量并重命名
from idcard import constant as const


class IdNumber(str):

    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        """根据区域编号取出区域名称"""
        return const.AREA_INFO[self.area_id]

    def get_birthday(self):
        """通过身份证号获取出生日期"""
        return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        """通过身份证号获取年龄"""
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day

        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        """通过身份证号获取性别， 女生：0，男生：1"""
        return int(self.id[16:17]) % 2

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def verify_id(cls, id_number):
        """校验身份证是否正确"""
        if re.match(const.ID_NUMBER_18_REGEX, id_number):
            check_digit = cls(id_number).get_check_digit()
            return str(check_digit) == id_number[-1]
        else:
            return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

    @classmethod
    def generate_id(cls, sex=0):
        """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""


        # 随机生成一个区域码(6位数)
        id_number = str(random.choice(list(const.AREA_INFO.keys())))
        # 限定出生日期范围(8位数)
        start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2020-12-30", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        # 顺序码(2位数)
        id_number += str(random.randint(10, 99))
        # 性别码(1位数)
        id_number += str(random.randrange(sex, 10, step=2))
        # 校验码(1位数)
        return id_number + str(cls(id_number).get_check_digit())
        random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
        return random_sex

#
if __name__ == '__main__':

    # 生成的身份证号
    id_card = IdNumber.generate_id()
    print('随机生成的有效身份证号是：',id_card)                          # 随机生成身份证号
    print('随机生成的区域编码是：',IdNumber(id_card).area_id)            # 地址编码
    print('随机生成的身份地址是：',IdNumber(id_card).get_area_name())    # 地址
    print('随机生成的身份生日是：',IdNumber(id_card).get_birthday())     # 生日
    print('随机生成的身份年龄是：',IdNumber(id_card).get_age())          # 年龄
    print('随机生成的身份性别是：',IdNumber(id_card).get_sex())          # 性别:奇数(男)，偶数（女）
    print('随机生成的末位校验码是：',IdNumber(id_card).get_check_digit())  # 校验码
    # print(IdNumber.verify_id(id_card))               # 检验身份证是否正确:False为失败
    # print(IdNumber.verify_id('451228195702216813'))
