# coding=utf-8
#!/usr/bin/python3
# @Time: 2021/6/8 15:21
# @Author: qinzhifeng
# @File: Beautifulsoup.py
# @Software: PyCharm

'''
    爬虫案例演示（BeautifulSoup）
'''

from bs4 import BeautifulSoup
import requests


# 1、接口请求和判断
url = 'http://www.crazyant.net/'
r = requests.get(url)
if r.status_code != 200:
    raise Exception()

html_doc = r.text   # html 文档字符串


# 2、创建 BeautifulSoup 对象
soup = BeautifulSoup(
    html_doc,                   # html 文档字符串
    'html.parser',              # html 解析器
    from_encoding = 'utf-8')    # html 文档的编码


# 3、在 html 文档中找到所有文章标题的节点位置，html 中，通过标签找到对应的父节点位置
#    通过 for 循环遍历所有的文章节点
h2_nodes = soup.find_all('h2', class_ = 'entry-title')
for h2_node in h2_nodes:
    link = h2_node.find('a')      # 寻找名称为 a 的节点
    print(link['href'], link.get_text())







