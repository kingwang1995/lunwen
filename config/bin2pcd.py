# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/8 13:37
# @File:bin2pcd.py
# @Software:PyCharm

import numpy as np

pointcloud = np.fromfile(str("000000.bin"), dtype=np.float32, count=-1).reshape([-1, 4])

x_points = pointcloud[:, 0]

y_points = pointcloud[:, 1]

z_points = pointcloud[:, 2]

r_points = pointcloud[:, 3]

f = open("p.txt", 'w')
for i in range(len(x_points)):
    line = str(x_points[i]) + ' ' + str(y_points[i]) + ' ' + str(z_points[i]) + ' ' + str(r_points[i]) + "\n"
    f.write(line)
