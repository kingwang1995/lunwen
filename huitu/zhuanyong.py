# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/7 16:58
# @File:zhuanyong.py
# @Software:PyCharm


# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']


def read():
    name_list = ['2015', '2016', '2017', '2018', '2019']

    time1 = [2, 4, 4, 8, 5]

    time2 = [2, 2, 2, 1, 0]

    time3 = [0, 0, 3, 5, 4]

    # time4 = [0.000, 0.000, 0.073, 0.021, 0.015]

    location = np.arange(len(name_list))

    width = 0.2

    plt.figure(figsize=(6, 4))

    plt.bar(location, time1, tick_label=name_list, width=width, label="图像", alpha=0.8, color="w", edgecolor="k",
            hatch="\\\\")

    for a, b in zip(location, time1):
        plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=7)

    plt.bar(location + width, time2, tick_label=name_list, width=width, label="体素", alpha=0.8, color="w",
            edgecolor="k", hatch=".....")

    for a, b in zip(location + width, time2):
        plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=7)

    plt.bar(location + width * 2, time3, tick_label=name_list, width=width, label="点云", alpha=0.8, color="w",
            edgecolor="k", hatch="/////")

    for a, b in zip(location + width * 2, time3):
        plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=7)

    # plt.bar(location + width * 3, time4, tick_label=name_list, width=width, label=">3", alpha=0.8, color="w",
    #         edgecolor="k", hatch="\\\\\\\\\\")
    #
    # for a, b in zip(location + width * 3, time4):
    #     plt.text(a, b + 0.05, '%.3f' % b, ha='center', va='bottom', fontsize=7)

    plt.ylim(0, 10)

    from matplotlib.font_manager import FontProperties
    font_set = FontProperties(fname=r"FZKTJW.TTF")

    plt.xlabel(u"年度", fontproperties=font_set)

    plt.ylabel(u'数量', fontproperties=font_set)
    plt.legend(loc=1)
    plt.savefig('result.png', dpi=200)

    plt.show()


if __name__ == '__main__':
    read()
