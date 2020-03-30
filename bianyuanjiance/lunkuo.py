# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/12 9:45
# @File:lunkuo.py
# @Software:PyCharm

import cv2

import numpy as np

import imutils

im = cv2.imread('img.jpg')

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 180, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 大津阈值

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # cv2.RETR_EXTERNAL 定义只检测外围轮廓

cnts = contours[1] if imutils.is_cv3() else contours[0]  # 用imutils来判断是opencv是2还是2+

# cnt = cnts[1]
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# cv2.drawContours(im, [box], 0, (0, 0, 255), 2)
list = []
for cnt in cnts:
    # 外接矩形框，没有方向角

    # x, y, w, h = cv2.boundingRect(cnt)
    #
    # cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 最小外接矩形框，有方向角

    rect = cv2.minAreaRect(cnt)
    list.append(rect)
    # box = cv2.boxPoints(rect)
    #
    # box = np.int0(box)
    #
    # cv2.drawContours(im, [box], 0, (0, 0, 255), 2)

max_rect = list[0]
for i in range(len(list)):
    ar = list[i][1][0] * list[i][1][1]
    max_ar = max_rect[1][0] * max_rect[1][1]
    if ar > max_ar:
        max_rect = list[i]

box = cv2.boxPoints(max_rect)
# 轮廓矩形
box_rect = np.int0(box)
# cv2.drawContours(im, [box_rect], 0, (255, 0, 255), 2)

# 检测框
box_dete = np.array([[129, 330], [129, 36], [380, 36], [380, 330]])
cv2.drawContours(im, [box_dete], 0, (0, 255, 0), 2)

# 矩形中心点
# x_max = max(box_rect[:, 0])
# x_min = min(box_rect[:, 0])
# y_max = max(box_rect[:, 1])
# y_min = min(box_rect[:, 1])
# x_rect = int((x_max - x_min) / 2) + x_min
# y_rect = int((y_max - y_min) / 2) + y_min
# print("初始值矩形：", x_rect, y_rect)
# cv2.circle(im, (x_rect, y_rect), 1, (255, 255, 0), 4)

# 检测框中心
x_max = max(box_dete[:, 0])
x_min = min(box_dete[:, 0])
y_max = max(box_dete[:, 1])
y_min = min(box_dete[:, 1])
x_dete = int((x_max - x_min) / 2) + x_min
y_dete = int((y_max - y_min) / 2) + y_min
print("初始值检测：", x_dete, y_dete)
cv2.circle(im, (x_dete, y_dete), 1, (255, 255, 0), 4)

box_rect = np.array([[250, 340], [129, 273], [272, 24], [393, 85]])
cv2.drawContours(im, [box_rect], 0, (0, 0, 255), 2)

# 矩形中心点
x_max = max(box_rect[:, 0])
x_min = min(box_rect[:, 0])
y_max = max(box_rect[:, 1])
y_min = min(box_rect[:, 1])
x_rect = int((x_max - x_min) / 2) + x_min
y_rect = int((y_max - y_min) / 2) + y_min
print("改动矩形：", x_rect, y_rect)
cv2.circle(im, (x_rect, y_rect), 1, (255, 0, 255), 4)

cv2.imshow('a', im)

# cv2.imwrite('res.jpg', im)

cv2.waitKey(0)
