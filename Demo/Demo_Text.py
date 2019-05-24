import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(.05, 10, 100)
y = np.sin(x)

plt.plot(x, y, ls="-.", c="c", label="plot figure")

plt.legend()

plt.text(3.10, 0.09, "y=sin(x)", weight="bold",color="b")

plt.show()

# plt.text(x, y, string, weight="bold", color="b")
# string 文本
# weight 文本粗细风格
# color  文本字体颜色


