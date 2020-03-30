# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/8 10:23
# @File:testp2i.py
# @Software:PyCharm

import matplotlib.pyplot as plt
import numpy as np
from config import point2img
import pcl

# lidar = pcl.load("or.pcd")
lidar = np.fromfile(str("000000.bin"), dtype=np.float32, count=-1).reshape([-1, 4])
HRES = 0.35  # horizontal resolution (assuming 20Hz setting)
VRES = 0.4  # vertical res
VFOV = (-24.9, 2.0)  # Field of view (-ve, +ve) along vertical axis
Y_FUDGE = 5  # y fudge factor for velodyne HDL 64E

point2img.lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="depth",
                                 saveto="lidar_depth.png", y_fudge=Y_FUDGE)

point2img.lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV, val="height",
                                 saveto="lidar_height.png", y_fudge=Y_FUDGE)

point2img.lidar_to_2d_front_view(lidar, v_res=VRES, h_res=HRES, v_fov=VFOV,
                                 val="reflectance", saveto="lidar_reflectance.png",
                                 y_fudge=Y_FUDGE)
