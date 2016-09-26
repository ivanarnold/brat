import numpy as np
import  matplotlib.pyplot as plt



level_dat = np.loadtxt('levels_more.dat')


plt.plot(level_dat[:,0], level_dat[:,1]*1.23981e4, 'k.')


