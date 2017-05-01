#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 仓库地址https://github.com/ObertShen/py_practice"""

__author__ = 'Shen'

import os
import urllib
from urlparse import urlsplit

from bs4 import BeautifulSoup


def catch_tieba_pics(url):
    """根据提供的贴吧url来抓取其中的图片"""
    content = urllib.urlopen(url)
    soup = BeautifulSoup(content, 'lxml')
    for i in soup.find_all('img', {"class": "BDE_Image"}):
        download_pic(i['src'])


def download_pic(url):
    """根据提供的文件获取地址下载文件"""
    image_content = urllib.urlopen(url).read()
    file_name = os.path.basename(urlsplit(url)[2])
    with open(file_name, 'wb') as output:
        output.write(image_content)



if __name__ == '__main__':
    catch_tieba_pics('http://tieba.baidu.com/p/2166231880')




