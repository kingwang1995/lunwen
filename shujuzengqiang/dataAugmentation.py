# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/9 9:39
# @File:dataAugmentation.py
# @Software:PyCharm
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import random

img = Image.open("img.jpg")
img = np.array(img)
plt.imshow(img)
plt.show()


def flip(img):
    flip_img = np.fliplr(img)
    cv2.imwrite("flip_img.jpg", flip_img)
    plt.imshow(flip_img)
    plt.show()


def translations(img):
    for j in range(416):
        for i in range(416):
            if (i < 416 - 20):
                img[j][i] = img[j][i + 20]
    cv2.imwrite("down.jpg", img)
    plt.imshow(img)
    plt.show()


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the rotation center
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def noising(image):
    # for i in range(1000):
    image[random.randint(0, image.shape[0] - 1)][random.randint(0, image.shape[1] - 1)][:] = 255
    plt.imshow(image)
    plt.show()


image = cv2.imread("img.jpg")
# noising(image)

contrast = 1  # 对比度
brightness = 100  # 亮度
pic_turn = cv2.addWeighted(image, contrast, image, 0, brightness)
cv2.imwrite("liangdu.jpg", pic_turn)
plt.imshow(pic_turn)
plt.show()

temp = cv2.GaussianBlur(image, (7, 7), 1.5)
cv2.imwrite("mohu.jpg", temp)
plt.imshow(temp)
plt.show()
# flip(img)
# translations(img)
# rotated = rotate(img, 90)
# cv2.imwrite("rotate.jpg", rotated)
# noised = noising(img)
# cv2.imwrite("noise.jpg", noised)
# plt.imshow(noised)
# plt.show()
