import matplotlib.pyplot as plt
import numpy as np

# 绘制刻度线曲线

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()
plt.grid(linestyle=":", color="r")

plt.show()