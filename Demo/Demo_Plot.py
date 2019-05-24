import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(.05, 10, 100)
y = np.cos(x)

plt.plot(x, y, ls="-", lw=2, label="plot figure")

plt.legend()

plt.show()
