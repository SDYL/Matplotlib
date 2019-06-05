# 绘制棉棒图

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 2*np.pi, 20)   # 指定棉棒在X轴上的位置
y = np.random.rand(20)              # 绘制棉棒长度


plt.stem(x, y, linefmt="-.", markerfmt="o", basefmt="-")
# [linefmt:棉棒的样式][markerfmt;棉棒末端样式][basefmt:指定基线样式]

plt.show()