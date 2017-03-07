#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Python 练习册 仓库地址https://github.com/ObertShen/show-me-the-code"""


__author__ = 'Shen'

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 该函数用于生成随机字符串
def _random_char():
    return random.choice(string.ascii_letters)

#  用于生成背景的随机颜色:
def _random_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#  生成随机颜色2:
def _random_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def generate_verification_code():
    """该函数用于生成验证码图片"""
    img_width = 60 * 4
    img_heigh = 60
    image = Image.new('RGB', (img_width, img_heigh), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for i in range(img_width):
        for j in range(img_heigh):
            draw.point((i, j), fill=_random_color())
    # 将文字打到图片上:
    for k in range(4):
        draw.text((60 * k + 10, 10), _random_char(), font=font, fill=_random_color2())
    # 模糊处理 让图片中的字母不易被识别:
    image = image.filter(ImageFilter.BLUR)
    image.save('result.jpg', 'jpeg')

if __name__ == '__main__':
    generate_verification_code()

