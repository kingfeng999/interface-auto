# coding=utf-8
#!/usr/bin/python3
# @Time: 2021/7/19 15:59
# @Author: qinzhifeng
# @File: 计算岗位金额.py
# @Software: PyCharm


def money_guding():
    '''
        计算发布岗位固定奖金金额，固定金额不能低于 30%，可以大于 30%
        固定奖金计算方式说明：
        薪酬范围：8000 ~ 10000
            固定奖金计算方式：(8000 + 9000 + 10000) / 3 * 0.3
    :return:
    '''

    # 动态输入薪资最小值和最大值，单位是元
    money_list = []
    min_money = int(input('输入固定奖金薪酬下限：'))
    max_money = int(input('输入固定奖金薪酬上限：'))
    money_list.append(min_money)
    money_list.append(max_money)
    print('岗位薪资范围是：', money_list)


    # 计算累加数据
    count = int((money_list[-1] - money_list[0]) / 1000) + 1
    print('薪资范围累加被除数为：', count)


    # 计算薪资范围总和
    sum = 0
    while money_list[0] <= money_list[0 + 1]:
        sum += money_list[0]
        money_list[0] += 1000
    print('薪资累加之和为：', sum)


    # 计算岗位固定奖金，单位是分，
    money = int(sum / count * 0.3) * 100
    print("固定奖金金额为（job/102 中 reward 的值）：", money)


    # 计算岗位预付总额，单位是分（3代表招聘人数，动态计算）
    total_money = money * 1
    print('岗位预付总额为（pay/100 中 price 和 total_free 的值）：',total_money)
    print("="*180)
    print()


def money_fudong():
    '''
        计算发布岗位浮动奖金金额范围
        浮动奖金计算方式说明：
            薪酬范围：8000 ~ 10000，15 薪
            浮动奖金计算方式：
            浮动奖金下限：8000 * 15 * 年收入比例（年收入比例范围：2.5% ~ 60%）
            浮动奖金上限：10000 * 15 * 年收入比例（年收入比例范围：2.5% ~ 60%）
    :return:
    '''

    # 动态输入薪资最小值和最大值
    print('****** ****** 浮动奖金比例范围是：2.5 ~ 60 % ****** ******')
    min_money = int(input('输入浮动奖金金额下限：'))
    max_money = int(input('输入浮动奖金金额上限：'))
    year_count = int(input('请输入年薪数：'))
    money_rate = float(input('请输入岗位年收入浮动奖金比例：'))


    str1 = '%'
    print('岗位的薪资范围是：{},{}'.format(min_money, max_money))
    print('岗位的年收入浮动奖金比例是：{}{}'.format(money_rate, str1))
    print('岗位的年薪数是(13~~30)：%d 薪' %(year_count))


    # 计算浮动奖金下限，单位：元
    money_down = int(min_money * year_count * money_rate / 100)
    print('岗位浮动奖金下限为：',money_down)

    # 计算浮动奖金上限，单位：元
    money_up = int(max_money * year_count * money_rate / 100)
    print('岗位浮动奖金下限为：', money_up)


if __name__ == '__main__':
    money_guding()
    # money_fudong()