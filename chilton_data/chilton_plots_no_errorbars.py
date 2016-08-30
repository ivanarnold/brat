# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:28:04 2016

@author: ivan
"""

import pylab as pl
import os

os.chdir('/home/ivan/Research/brat/chilton_data')

# %% 1p0 --> 2p10

pl.clf()
ourdat  = pl.loadtxt('1p0_2p10_J1.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 4.7, 'bs', ms=5)
pl.plot(20.0, 1.4, 'bo', ms=5)

#errorbar = pl.errorbar(20, 4.7, yerr=2.2, ls="None", color = 'b')
#pl.plot(40.0, 2.5, 'bs', ms=3)
#errorbar = pl.errorbar(40, 2.5, yerr=1.0, ls="None", color = 'b')
#pl.plot(40.0, 5.2, 'r^', ms=5)
#pl.plot(40.0, 2.8, 'go', ms=3)


pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p10 (J=1)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1p0 --> 2p9

pl.clf()
ourdat  = pl.loadtxt('1p0_2p9_J3.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 5.3, 'bs', ms=5)
pl.plot(20.0, 3.9, 'bv', ms=5)
pl.plot(20.0, 2.4, 'bo', ms=5)


#errorbar = pl.errorbar(20, 5.3, yerr=2.2, ls="None", color = 'b')
#pl.plot(40.0, 0.63, 'bs', ms=3)
#errorbar = pl.errorbar(40, 0.63, yerr=0.5, ls="None", color = 'b')
#pl.plot(40.0, 3.2, 'r^', ms=5)
#pl.plot(40.0, 2.6, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p9 (J=3)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1p0 --> 2p8

pl.clf()
ourdat  = pl.loadtxt('1p0_2p8_J2.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 5.4, 'bs', ms=5)
pl.plot(20.0, 2.4, 'bv', ms=5)
pl.plot(20.0, 1.3, 'bo', ms=5)
#errorbar = pl.errorbar(40, 2.6, yerr=0.8, ls="None", color = 'b')
#pl.plot(40.0, 4.7, 'r^', ms=5)
#pl.plot(40.0, 2.0, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p8 (J=2)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p7

pl.clf()
ourdat  = pl.loadtxt('1p0_2p7_J1.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')


pl.plot(20.0, 2.5, 'bs', ms=5)
pl.plot(20.0, 1.9, 'bv', ms=5)
pl.plot(20.0, 1.4, 'bo', ms=5)
#errorbar = pl.errorbar(20, 2.5, yerr=0.9, ls="None", color = 'b')
#pl.plot(40.0, 1.5, 'bs', ms=3)
#errorbar = pl.errorbar(40, 1.5, yerr=0.3, ls="None", color = 'b')
#pl.plot(40.0, 2.9, 'r^', ms=5)
#pl.plot(40.0, 1.4, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p7 (J=1)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p6

pl.clf()
ourdat  = pl.loadtxt('1p0_2p6_J2.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')


pl.plot(20.0, 3.2, 'bs', ms=5)
pl.plot(20.0, 1.7, 'bv', ms=5)
pl.plot(20.0, 1.5, 'bo', ms=5)
#errorbar = pl.errorbar(20, 3.2, yerr=1.2, ls="None", color = 'b')
#pl.plot(40.0, 2.2, 'bs', ms=3)
#errorbar = pl.errorbar(40, 2.2, yerr=0.7, ls="None", color = 'b')
#pl.plot(40.0, 4.2, 'r^', ms=5)
#pl.plot(40.0, 2.0, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p6 (J=2)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p5

pl.clf()
ourdat  = pl.loadtxt('1p0_2p5_J0.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')


pl.plot(20.0, 5.3, 'bs', ms=5)
pl.plot(20.0, 3.9, 'bv', ms=5)
pl.plot(20.0, 2.4, 'bo', ms=5)
#errorbar = pl.errorbar(20, 1.6, yerr=0.4, ls="None", color = 'b')
#pl.plot(40.0, 1.4, 'bs', ms=3)
#errorbar = pl.errorbar(40, 1.4, yerr=0.4, ls="None", color = 'b')
#pl.plot(40.0, 1.9, 'r^', ms=5)
#pl.plot(40.0, 0.67, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p5 (J=0)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=4)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p4

pl.clf()
ourdat  = pl.loadtxt('1p0_2p4_J1.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 2.2, 'bs', ms=5)
pl.plot(20.0, 1.7, 'bv', ms=5)

#errorbar = pl.errorbar(20, 2.2, yerr=0.7, ls="None", color = 'b')
#pl.plot(40.0, 0.9, 'bs', ms=3)
#errorbar = pl.errorbar(40, 0.9, yerr=0.37, ls="None", color = 'b')
#pl.plot(40.0, 1.9, 'r^', ms=5)
#pl.plot(40.0, 1.0, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p4 (J=1)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p3

pl.clf()
ourdat  = pl.loadtxt('1p0_2p3_J2.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 2.9, 'bs', ms=5)
pl.plot(20.0, 3.7, 'bv', ms=5)
pl.plot(20.0, 1.1, 'bo', ms=5)
#errorbar = pl.errorbar(20, 2.9, yerr=1.7, ls="None", color = 'b')
#pl.plot(40.0, 1.7, 'bs', ms=3)
#errorbar = pl.errorbar(40, 1.7, yerr=0.6, ls="None", color = 'b')
#pl.plot(40.0, 3.2, 'r^', ms=5)
#pl.plot(40.0, 1.6, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p3 (J=2)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=1)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p2

pl.clf()
ourdat  = pl.loadtxt('1p0_2p2_J1.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 1.4, 'bs', ms=5)
pl.plot(20.0, 1.8, 'bv', ms=5)
pl.plot(20.0, 0.58, 'bo', ms=5)
#errorbar = pl.errorbar(20, 1.4, yerr=0.6, ls="None", color = 'b')
#pl.plot(40.0, 0.9, 'bs', ms=3)
#errorbar = pl.errorbar(40, 0.9, yerr=0.45, ls="None", color = 'b')
#pl.plot(40.0, 2.1, 'r^', ms=5)
#pl.plot(40.0, 1.2, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p2 (J=1)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=2)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()

# %% 1p0 --> 2p1

pl.clf()
ourdat  = pl.loadtxt('1p0_2p1_J0.dat')

ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(20.0, 5.0, 'bs', ms=5)
pl.plot(20.0, 5.2, 'bv', ms=5)
pl.plot(20.0, 2.7, 'bo', ms=5)
#errorbar = pl.errorbar(20, 5.0, yerr=0.7, ls="None", color = 'b')
#pl.plot(40.0, 3.1, 'bs', ms=3)
##errorbar = pl.errorbar(40, 3.1, yerr=0.5, ls="None", color = 'b')
#pl.plot(40.0, 0.63, 'go', ms=3)

pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p1 (J=0)')
pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)

pl.legend(loc=2)
pl.xlim([10,35])
pl.ylim(ymin=0.0)

pl.show()
