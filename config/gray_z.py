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
minx = 0
maxx = 12000.0
miny = 4600
maxy = 11000.0
filename1 = 'points1.txt'
filename2 = 'points2.txt'
with open(filename1, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
            pass
        x, y, z = [float(i) for i in lines.split(' ')]
        if x >= minx and x < maxx and y >= miny and y < maxy and z >= 50. and z < 2000.:
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
        if x >= minx and x < maxx and y >= miny and y < maxy and z >= 50. and z < 2000.:
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
width = 416 * 2
height = 208 * 2
w = []
h = []
im = []
img = np.zeros([width, height * 2])
for i in range(len(xlist)):
    c = int((xlist[i] - minx) / (maxx - minx) * width)
    r = int((ylist[i] - miny) / (maxy - miny) * height)
    w.append(c)
    h.append(r)
    gray = int(zlist[i] / 2000. * 256)
    if gray > img[r, c]:
        img[r, c] = gray
print(img)
np.savetxt('file.txt', img, fmt="%d")
cv2.imwrite("img.jpg", img)
cv2.imshow("img", img)
cv2.waitKey()
# plt.imshow(img, cmap="nipy_spectral")
# plt.show()
