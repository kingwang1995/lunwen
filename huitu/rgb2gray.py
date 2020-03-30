# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/21 20:30
# @File:rgb2gray.py
# @Software:PyCharm

import cv2

fname = "aa.png"
img = cv2.imread(fname)
print(img.size)
cv2.resize(img, (400, 600))
I1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
I2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('gray', I1)
cv2.imshow('hsv', I2)
cv2.imwrite("gray_aa.jpg", I1)
cv2.waitKey()
