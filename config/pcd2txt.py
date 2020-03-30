# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/19 8:37
# @File:pcd2txt.py
# @Software:PyCharm

import pcl
import random

p = pcl.load('af.pcd')
listx = []
listy = []
listz = []
# 读取pcd文件#写入文件
f = open('af.txt', 'w')
for i in range(p.size):
    f.write(str(p[i][0]) + ' ' + str(p[i][1]) + ' ' + str(p[i][2]) + '\n')
    listx.append(p[i][0])
    listy.append(p[i][1])
    listz.append(p[i][2])

for j in range(10500):
    x = (listx[j] + listx[j + 1]) / 2.
    y = (listy[j] + listy[j + 1]) / 2.
    z = (listz[j] + listz[j + 1]) / 2.
    f.write(str(x) + ' ' + str(y) + ' ' + str(z) + '\n')
f.close()
