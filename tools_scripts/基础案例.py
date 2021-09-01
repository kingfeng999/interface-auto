# coding=utf-8
#!/usr/bin/python3
# @Time: 2021-09-01 16:31
# @Author: qinzhifeng
# @File: 基础案例.py
# @Software: PyCharm

'''
    自动化班编程基础案例讲解
'''

# 将列表中的大写字母改为小写，数字和 None 保持不变
a1 = ['Hello', 'World', 898, None]
a11 = []
for i in a1:
    if isinstance(i, str):  # isinstance 方法可以判断列表元素的类型
        a = i.lower()       # 将大写字母转换为小写
        a11.append(a)       # 如果元素是字符串类型，则加入到新列表中
    else:
        a11.append(i)       # 如果不是字符串类型，则直接加入新的列表中
print(a11)


# 过滤列表中重复的元素，并将重复元素出现的个数打印出来
a2 = [1,1,1,3,3,5,0,0,0,8,8,8,8,10]
li = list(set(a2))      # 集合去重后转换为 list
print('去重后的列表数据为：', li)
for i in li:
    print('元素{}在列表中出现的次数为：{}次'.format(i, a2.count(i)))


# 算法去重
li = [1, 3, 4, 5, 5, 5, 5, 5]
new_dict = {}.fromkeys(li,'1')
li = list(new_dict)
print(li)


li = [1, 3, 4, 5, 5, 5, 5, 5]
new_li = []
for id in li:
 if id not in new_li:
  new_li.append(id)
print(new_li)


li=[5,5,1,3,4, 5,5,5]
new_li = list(set(li))
print(new_li)


# 冒泡排序
maopao = [89, 3, 45, 30, 99, 190, 67]

for i in range(len(maopao)):
    for j in range(len(maopao) - i - 1):
        if maopao[j] > maopao[j + 1]:
            maopao[j + 1], maopao [j] = maopao[j], maopao[j + 1]
print(maopao)


# 九九乘法表
# 定义乘法表行数
for i in range(1, 10):

    # 定义乘法表列数
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')       # end=''，末尾不换行，添加一个空格
    print()


# 计算列表中元素的和
a = [1,2,5,10]
sum = 0
# for i in range(0,len(a)):
#     sum+=a[i]

for i in range(len(a)):
    sum+=a[i]

print('100以内偶数的和为：',sum)


'''
    需求说明：
    给定一个整数列表 num 和一个目标值 target，请你在该数组中找出差为目标值的所有数组，并返回每组整数下标
    示例：
    列表：num = [2, 7, 11, 13]
    目标值：target = 4
    因为 num [2] - num[1] = 11 - 7 = 4
    所以返回下标：[[2,1]]
'''

num = [2, 7, 11, 13, 15, 17]
target = 4
new_num = []

for i in range (0, len(num)):
    for j in range (0, len(num)):
        if num[i] - num[j] == target:
            new_num.append([i,j])

print(new_num)


def test(target):
    testlist = [1, 3, 5, 6, 10, 20, 18, 18]
    list2 = []
    for i in range(0, len(testlist)):
        for j in range(0, len(testlist)):
            if testlist[i] - testlist[j] == target:
                list2.append([i, j])
    return list2

if __name__ == '__main__':
    a = test(5)
    print(a)