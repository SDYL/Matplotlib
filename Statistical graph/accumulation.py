# 绘制柱状统计图形
# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 完成字体配置任务
mpl.rcParams["axes.unicode_minus"] = False

# some simple data

x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3,  8, 5]

bar_width = 0.35
tick_label = ["A", "B", "C", "D", "E"]

# creat bar
plt.bar(x, y, bar_width, align="center", color="c",
        label="班级A",
        alpha=0.5)
plt.bar(x+bar_width, y1, bar_width, align="center", color="b",
        label=" 班 级B",
        alpha=0.5)
# x 柱状图中柱体的标签值
# y 柱体高度
# align 柱体对齐方式
# alpha = 透明度

# set x, y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis grid

# plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)
plt.xticks(x + bar_width / 2, tick_label)
plt.legend()
plt.show()
