# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/7 16:18
# @File:zhuzhuangtu.py
# @Software:PyCharm

import numpy as np
import matplotlib.pyplot as plt

##-----读取数据----------
name = [2015, 2016, 2017, 2018, 2019]
VI = [2, 4, 4, 8, 5]
VC = [2, 2, 2, 1, 0]
VP = [0, 0, 3, 5, 4]

##-----绘制右边柱子----------
##w是柱子的宽度
w = 1
##生成绘图对象
fig = plt.figure()
##将画布划分成1行1列，在第一个方格中绘制
ax1 = fig.add_subplot(111)
##隐藏上边框
ax1.spines['top'].set_color('none')
##设置刻度范围
ax1.set_ylim(0, max(VC))
##设置x轴为下边框
ax1.xaxis.set_ticks_position('bottom')
##将x轴移动至0刻度处
ax1.spines['bottom'].set_position(('data', 0))
##设置x轴的标签，3个单位长度间隔，和柱子间距一致
##ax1.set_xticks(np.arange(0,len(name)*3,3))
ax1.set_xticklabels(name, ha='left', fontsize=9)
##设置柱子间距
idx = np.arange(w, len(name) * 3 + w, 3)
##生成柱状图，VI是数据列，width是柱子宽度
plt.bar(idx, VC, width=w, color='red')

##-----绘制左边柱子----------
##共享x坐标，这是关键
ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylim(0, max(VI))
ax2.set_xticks(np.arange(0, len(name) * 3, 3))
ax2.set_xticklabels(name, ha='left', fontsize=9)

plt.bar(idx - w, VI, width=w)

##-----绘制左边柱子----------
##共享x坐标，这是关键
ax2 = ax1.twinx()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylim(0, max(VI))
ax2.set_xticks(np.arange(0, len(name) * 3, 3))
ax2.set_xticklabels(name, ha='left', fontsize=9)

plt.bar(idx - w, VP, width=w)
plt.show()
