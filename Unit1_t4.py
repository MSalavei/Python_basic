import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
k1 = 1
k2 = 5
plt.plot(x, np.cos(k1 * x))
plt.plot(x, np.cos(k2 * x))
plt.show()
