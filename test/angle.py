# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/11 20:48
# @File:angle.py
# @Software:PyCharm
import math


def angleCom(x, y):
    a = math.atan2(y, x) * 180 / math.pi
    if (a >= 0. and a < 180):
        a = 180 - a
    else:
        a = 180 + a
    return a


y = 6150
x = 933
angle = angleCom(y, x)
print(angle)
