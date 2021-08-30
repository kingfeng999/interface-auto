# -*- coding:utf-8 -*-
#!/usr/bin/python3
# @Time: 2021/1/26 5:19 下午
# @Author: zhifeng.qin
# @File: 读取 yaml 数据.py
# @Software: PyCharm

import yaml
class ReadYaml:

    def get_yaml(self, key):
        '''
        解析 yaml、yml 文件，得到列表嵌套字典的数据格式
        =========================
        以下是读取 json 的命令
        json.load()  读
        json.dump()  写
        =========================
        以下是读取 yaml 的命令
        yaml.safe_load()
        :return:
        '''

        with open('./login_data.yaml', encoding = 'utf-8') as f:
            # 读取 yaml 文件，得到列表嵌套字典的数据格式
            yaml_data = yaml.safe_load(f)
            print(yaml_data)

            # 第一种方式读取文件（通过 list 进行转换）
            # cases_dict = yaml_data.get(key)
            # case_object = cases_dict.values()
            # data = list(case_object)
            # return data

            # 第二种方式读取文件（通过 extend ）
            data_list = []                       # 创建一个空列表
            cases_dict = yaml_data.get(key)      # 动态传参，用 key，获取 key
            case_object = cases_dict.values()    # 获取 key 对应的值，实际上获取到的只是一个可迭代对象
            data_list.extend(case_object)
            return data_list

            # 第三种方式读取文件（for...in...）
            # cases_dict = yaml_data.get(key)
            # case_object = cases_dict.values()
            # for i in case_object:
            #     print(i)
            # return


if __name__ == '__main__':
    # 'test_login' 为 yaml 文件中第一行的数据
    print(ReadYaml().get_yaml('test_login'))


