#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 仓库地址https://github.com/ObertShen/py_practice"""

__author__ = 'Shen'

import os
from PIL import Image, ImageDraw, ImageFont

def add_num(image, text):
    """该函数在图片的右上角绘制数字"""
    print image.mode, image.size, image.format, image.height, image.width
    drawable = ImageDraw.Draw(image)
    font_size = image.height/4
    if image.height > image.width:
        font_size = image.width/4

    tt_font = ImageFont.truetype("Arial.ttf", font_size)
    drawable.text((image.width-font_size, 0),
                  text, fill=(255, 0, 0), font=tt_font)
    # image.show()

if __name__ == '__main__':
    IMAGE = Image.open(os.path.dirname(__file__)+'/avatar.jpg')
    add_num(IMAGE, '7')
    IMAGE.save(os.path.dirname(__file__)+'/result.jpg', 'jpeg')

