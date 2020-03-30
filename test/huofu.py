# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/11 20:57
# @File:huofu.py
# @Software:PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1.加载图片，转为二值图
img = cv2.imread('img.jpg')
drawing = np.zeros(img.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 50, 150)

# 2.霍夫直线变换
lines = cv2.HoughLines(edges, 1, np.pi / 180, 90)
# 3.将检测的线画出来（注意是极坐标噢）
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
cv2.imshow('img', drawing)
cv2.imshow('img_', edges)
cv2.waitKey()
