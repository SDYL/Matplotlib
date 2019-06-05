# 绘制直方图
# 未解决问题，每个数据单元没有分隔线
# -*- coding:utf-8 -*-

import matplotlib as mpl

import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set test scores
boxWeight = np.random.randint(0, 10, 100)

x = boxWeight
# plot histogram
bins = range(0, 11, 1)

plt.hist(x, bins=bins,
         color="g",
         histtype="bar",
         rwidth=1,
         alpha=0.6)

# set x, y-axis label

plt.xlabel("箱子重量(kg)")
plt.ylabel("销售数量(个)")

plt.show()
