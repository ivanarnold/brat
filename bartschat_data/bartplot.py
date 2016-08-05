# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:02:57 2016

@author: ivan
"""

import pylab as pl
import os

pl.rcParams['legend.numpoints'] = 1

os.chdir('/home/ivan/Dropbox/Research/ELEX/brat/bartschat_data')

# %% 1s5 --> 2p10

pl.clf()
bartdat = pl.loadtxt('s5_2p10.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p10_J1.dat')
#boffdat = pl.loadtxt('../piech_data/s5_2p10_j3.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

ax1.annotate('$2p10 \quad (J=1)$', xy=(300, 200), xycoords='axes points',
            size=14, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))

pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1s5 --> 2p9

pl.clf()
bartdat = pl.loadtxt('s5_2p9.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p9_J1.dat')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
           
ax1.annotate('$2p9 \quad (J=3)$', xy=(300, 200), xycoords='axes points',
            size=14, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1s5 --> 2p8

pl.clf()
bartdat = pl.loadtxt('s5_2p8.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p8_J0.dat')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
           
ax1.annotate('$2p8 \quad (J=2)$', xy=(300, 200), xycoords='axes points',
            size=14, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1s5 --> 2p7

pl.clf()
bartdat = pl.loadtxt('s5_2p7.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p7_J1.dat')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()

# %%

# %% 1s5 --> 2p6

pl.clf()
bartdat = pl.loadtxt('s5_2p6.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p6_J0.dat')
boffdat = pl.loadtxt('../piech_data/s5_2p6_j2.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s5 --> 2p5

pl.clf()
bartdat = pl.loadtxt('s5_2p5.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p5_J2.dat')
boffdat = pl.loadtxt('../piech_data/s5_2p5_j0.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4, label='2p5')
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)
pl.legend(loc=1)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s5 --> 2p4

pl.clf()
bartdat = pl.loadtxt('s5_2p4.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p4_J1.dat')
boffdat = pl.loadtxt('../piech_data/s5_2p4_j1.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s5 --> 2p3

pl.clf()
bartdat = pl.loadtxt('s5_2p3.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p3_J0.dat')
boffdat = pl.loadtxt('../piech_data/s5_2p3_j2.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s5 --> 2p2

pl.clf()
bartdat = pl.loadtxt('s5_2p2.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p2_J1.dat')
boffdat = pl.loadtxt('../piech_data/s5_2p2_j1.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.548, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.548, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s5 --> 2p1

pl.clf()
bartdat = pl.loadtxt('s5_2p1.txt')
ourdat  = pl.loadtxt('../piech_data/1s5_2p2_J1.dat')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.548, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()
# %%

# %% 1s3 --> 2p4

pl.clf()
bartdat = pl.loadtxt('s3_2p4.txt')
ourdat  = pl.loadtxt('../piech_data/1s3_2p4_J1.dat')
boffdat = pl.loadtxt('../piech_data/s3_2p4_j1.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.728, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.728, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.728, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)


pl.xlim([0,30])

pl.show()
# %%

# %% 1s3 --> 2p4

pl.clf()
bartdat = pl.loadtxt('s3_2p2.txt')
ourdat  = pl.loadtxt('../piech_data/1s3_2p2_J1.dat')
boffdat = pl.loadtxt('../piech_data/s3_2p2_j1.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')

pl.plot(bartdat[:,0]-11.728, bartdat[:,1] * 100, 'ks', ms=4)
pl.plot(bartdat[:,2]-11.728, bartdat[:,3] * 100, 'ro')
pl.plot(ourdat[:,0], ourdat[:,2], 'b.', ms=5)

errorbar = pl.errorbar(bartdat[:,2]-11.728, bartdat[:,3] * 100, bartdat[:,3] \
           * 100 * 0.4, linestyle='None', color='red')
#pl.plot(boffdat[:,0], boffdat[:,1] * 100, 'gs', ms=5)
pl.xlim([0,30])
pl.ylim(ymin=0.0)

pl.show()

# %%