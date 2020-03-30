# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/2/24 10:45
# @File:display.py
# @Software:PyCharm

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datareader

x, y, z = datareader.DataReader()
# 开始绘图
fig = plt.figure(dpi=120)
ax = fig.add_subplot(111, projection='3d')
# 标题
plt.title('point cloud')
# 利用xyz的值，生成每个点的相应坐标（x,y,z）
ax.scatter(x, y, z, c='b', marker='.', s=2, linewidth=0, alpha=1, cmap='spectral')
ax.axis('scaled')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# 显示
plt.show()
