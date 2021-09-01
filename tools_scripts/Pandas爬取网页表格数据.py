# coding=utf-8
#!/usr/bin/python3
# @Time: 2021/6/7 10:29
# @Author: qinzhifeng
# @File: Pandas爬取网页表格数据.py
# @Software: PyCharm

import pandas as pd


'''
    用 Pandas 批量爬取网页表格所有数据
'''
df = pd.DataFrame()
for i in range(1, 48):
    url = f'http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml?p={i}'
    df = pd.concat([df, pd.read_html(url)[0]])  # 爬取 + 合并DataFrame
    print(df)

print("*"*88)

'''
    通过 pd.read_html 爬取单个表格的数据，header=0 指定列标题所在的行
'''
df = pd.read_html("http://www.air-level.com/air/beijing/", encoding='utf-8',header=0)[0]
print(df)

