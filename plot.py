import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Qt5Agg')


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
ypoints2 = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.plot(ypoints2, linestyle = 'dotted')
plt.show()