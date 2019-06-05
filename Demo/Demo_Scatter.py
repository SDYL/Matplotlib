# 绘制气泡图
# plt.scatter(x,y)

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a = np.random.rand(100)
b = np.random.rand(100)

# colormap:RdYlBu
plt.scatter(a, b, s=np.power(10*a+20*b, 2),
            c = np.random.rand(100),
            cmap=mpl.cm.RdYlBu,
            marker="o")

plt.show()