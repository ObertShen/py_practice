#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 第一题：生成 200个激活码（或者优惠券） 仓库地址https://github.com/ObertShen/py_practice"""



__author__ = 'Shen'

import string
import random

SEED = string.ascii_letters + "0123456789"

def generate_random_string(length):
    """生成固定长度随机字符串的函数"""
    random_string = ""
    for _ in range(length):
        random_string += random.choice(SEED)
    return random_string

if __name__ == '__main__':
    for _ in range(200):
        print generate_random_string(20)
