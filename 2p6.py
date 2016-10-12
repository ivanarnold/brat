import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('1p0_2p6_J2.dat')

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])

plt.show()
