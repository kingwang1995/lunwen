# -*-coding:utf-8 -*-
# @Author:king
# @time:2020/3/21 20:07
# @File:rect.py
# @Software:PyCharm

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator

fname = "20180809_132621.jpg"
img = np.array(Image.open(fname))
plt.figure()
fig,ax = plt.subplots(1)
ax.imshow(img)
x1, y1, x2, y2 = 216, 36, 334, 160
box_w = x2-x1
box_h = y2-y1

bbox = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, edgecolor="red", facecolor="none")
ax.add_patch(bbox)
plt.text(x1, y1, s="", color="white", verticalalignment="top",bbox={"color": "red", "pad": 0})
plt.axis("off")
plt.gca().xaxis.set_major_locator(NullLocator())
plt.gca().yaxis.set_major_locator(NullLocator())
filename = "c"
plt.savefig(f"{filename}.jpg", bbox_inches="tight", pad_inches=0.0)
plt.close()