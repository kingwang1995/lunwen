# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/11 21:06
# @File:huofu2.py
# @Software:PyCharm
import cv2
import numpy as np

# 渐进概率式霍夫变换

img = cv2.imread('img.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img, 50, 250)

lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 20, minLineLength=250, maxLineGap=100)

lines = lines[:, 0, :]
[x1, y1, x2, y2] = lines[0]
cv2.line(img,(x1, y1), (x2, y2), (0, 255, 0), 2)
# for x1, y1, x2, y2 in lines:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imshow('img', img)
cv2.imwrite('huofu.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
