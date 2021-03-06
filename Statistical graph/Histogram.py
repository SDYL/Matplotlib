# 绘制柱状统计图形
# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 完成字体配置任务
mpl.rcParams["axes.unicode_minus"] = False

# some simple data

x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# creat bar
plt.bar(x, y, align="center", color="b",
        tick_label=["A", "B", "C", "D", "E"],
        alpha=0.5)
# x 柱状图中柱体的标签值
# y 柱体高度
# align 柱体对齐方式
# alpha = 透明度

# set x, y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

# set yaxis grid

plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.show()
