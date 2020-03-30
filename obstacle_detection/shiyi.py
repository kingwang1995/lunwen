# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/14 9:44
# @File:shiyi.py
# @Software:PyCharm

import matplotlib.pyplot as plt
import numpy as np
import random

y = []
x = np.linspace(0, 361, 361)
for i in range(140):
    y.append(random.randint(630, 645))
for i in range(140, 180):
    y.append(random.randint(330, 345))
for i in range(180, 361):
    y.append(random.randint(630, 645))
plt.plot(x, y)
plt.xlim(0, 400)
plt.ylim(0, 810)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("y.jpg", dpi=100)
plt.show()
