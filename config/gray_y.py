# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/8 13:50
# @File:gray_z.py
# @Software:PyCharm

import numpy as np
import cv2
import matplotlib.pyplot as plt

xlist = []
ylist = []
zlist = []

filename1 = 'pts1.txt'
filename2 = 'pts2.txt'
with open(filename1, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
            pass
        x, y, z = [float(i) for i in lines.split(' ')]
        if x >= -10000 and x < 12000 and y >= -20000 and y < 50000 and z >= 50. and z < 2000.:
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
with open(filename2, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
            pass
        x, y, z = [float(i) for i in lines.split(' ')]
        if x >= -10000 and x < 12000 and y >= -20000 and y < 50000 and z >= 50. and z < 2000.:
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
minx = min(xlist)
maxx = max(xlist)
miny = min(ylist)
maxy = max(ylist)
minz = 0
maxz = 2000
res = 0.1

width = 416 * 2
height = 416 * 2
w = []
h = []
im = []
img = np.zeros([1 + width, 1 + height])
for i in range(len(xlist)):
    c = int((xlist[i] - minx) / (maxx - minx) * width)
    r = int((ylist[i] - miny) / (maxy - miny) * height)
    w.append(c)
    h.append(r)
    gray = int(zlist[i] / 2000. * 256)
    if gray > img[r, c]:
        img[r, c] = gray
# print(img)
# cv2.imwrite("img.jpg", img)
cv2.imshow("img", img)
cv2.waitKey()
# plt.imshow(img, cmap="nipy_spectral")
# plt.show()
