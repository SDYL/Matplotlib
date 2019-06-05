# 绘制极线图
# 功能，在极坐标上绘制折线图
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
r = 30*np.random.rand(barSlices)            # r 标记到原点的距离

plt.polar(theta, r, color="chartreuse",     # theta 明日歌标记所在射线与极经的夹角
          linewidth=2,
          marker="*",
          mfc="b",
          ms=10
          )

plt.show()