# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/7 16:58
# @File:zhuanyong.py
# @Software:PyCharm

import numpy as np

import matplotlib.pyplot as plt

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']


def read():
    name_list = ['车辆1', '车辆2']

    time1 = [35.24, 23.59]

    time2 = [32.86, 22.15]

    # time3 = [0, 0, 3, 5, 4]

    # time4 = [0.000, 0.000, 0.073, 0.021, 0.015]

    location = np.arange(len(name_list))

    width = 0.2

    plt.figure(figsize=(6, 4))

    plt.bar(location, time1, tick_label=name_list, width=width, label="法向夹角方法", alpha=0.8, color="w", edgecolor="k",
            hatch="\\\\")

    for a, b in zip(location, time1):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    plt.bar(location + width, time2, tick_label=name_list, width=width, label="本文方法", alpha=0.8, color="w",
            edgecolor="k", hatch=".....")

    for a, b in zip(location + width, time2):
        plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize=7)

    # plt.bar(location + width * 2, time3, tick_label=name_list, width=width, label="点云", alpha=0.8, color="w",
    #         edgecolor="k", hatch="/////")
    #
    # for a, b in zip(location + width * 2, time3):
    #     plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=7)

    # plt.bar(location + width * 3, time4, tick_label=name_list, width=width, label=">3", alpha=0.8, color="w",
    #         edgecolor="k", hatch="\\\\\\\\\\")
    #
    # for a, b in zip(location + width * 3, time4):
    #     plt.text(a, b + 0.05, '%.3f' % b, ha='center', va='bottom', fontsize=7)

    plt.ylim(0, 50)

    from matplotlib.font_manager import FontProperties
    font_set = FontProperties(fname=r"FZKTJW.TTF")

    plt.xlabel(u"车辆模型", fontproperties=font_set)

    plt.ylabel(u'耗时', fontproperties=font_set)
    plt.legend(loc=1)
    plt.savefig('result.png', dpi=200)

    plt.show()


if __name__ == '__main__':
    read()
