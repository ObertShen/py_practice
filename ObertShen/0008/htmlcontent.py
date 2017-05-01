#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 第8题 获取HTML文件的正文 仓库地址https://github.com/ObertShen/py_practice"""

__author__ = 'Shen'

import urllib

from bs4 import BeautifulSoup

def catch_html_content_text(url):
    """根据提供的url来获取该html的正文内容"""
    content = urllib.urlopen(url)
    soup = BeautifulSoup(content, 'lxml')
    return soup.body.text


if __name__ == '__main__':
    print catch_html_content_text('http://www.baidu.com')
