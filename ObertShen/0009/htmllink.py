#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 第8题 获取HTML文件的链接 仓库地址https://github.com/ObertShen/py_practice"""

__author__ = 'Shen'

import urllib

from bs4 import BeautifulSoup

def catch_html_link(url):
    """根据提供的url来获取该html文件的链接内容"""
    content = urllib.urlopen(url)
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all(href=True)
    # print soup.body.text
    for i in links:
        print i['href']

if __name__ == '__main__':
    catch_html_link('http://www.baidu.com')
