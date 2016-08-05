# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:28:04 2016

@author: ivan
"""

import pylab as pl
import os

os.chdir('/home/ivan/Dropbox/Research/ELEX/brat/chilton_data')

# %% 1p0 --> 2p10

pl.clf()
childat = pl.loadtxt('2p10_j1.dat')
ourdat  = pl.loadtxt('../chilton_data/1p0_2p10_J1.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(childat[:,0], childat[:,1] / 10, 'ks', ms=3)
pl.plot(ourdat[:,0], ourdat[:,1], 'b', ms=3)
pl.plot(ourdat[:,0], ourdat[:,2], 'r--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.xlim([10,40])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1p0 --> 2p9

pl.clf()
childat = pl.loadtxt('2p9_j3.txt')
ourdat  = pl.loadtxt('../chilton_data/1p0_2p9_J3.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(childat[:,0], childat[:,1] / 10, 'ro', ms=3)
#pl.plot(childat[:,2], childat[:,3] / 10, 'bs', ms=3)
pl.plot(childat[:,4], childat[:,5] / 10, 'gs', ms=3)

pl.plot(18, 5.3, 'b>', ms=10)
errorbar = pl.errorbar(18, 5.3, yerr=2.2, ls="None", color = 'b')
pl.plot(18 + 0.4, 3.9, 'b<', ms=10)
errorbar = pl.errorbar(18 + 0.4, 3.9, yerr=1.2, ls="None", color = 'b')

pl.plot(40, 3.2, 'r*')
#errorbar = pl.errorbar(40, 3.2, yerr=0.4, ls="None", color = 'r')
pl.plot(40, 2.6, 'g*')
#errorbar = pl.errorbar(40, 2.6, yerr=0.3, ls="None", color = 'g')

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3)
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.xlim([10,43])
pl.ylim(ymin=0.0)

pl.show()

# %%