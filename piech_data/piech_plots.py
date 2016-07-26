# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:02:57 2016

@author: ivan
"""

# %% INIT
import pylab as pl
import os
os.chdir('/home/ivan/Dropbox/Research/ELEX/brat/piech_data')

#==============================================================================
# %% cell0
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s5_2p10_J1.dat', dtype = 'float')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s5$ ' r'$\rightarrow$'  '$2p10$ ' '($\Delta J=1)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')

pl.show()



#==============================================================================
# %% cell1
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s5_2p9_J1.dat', dtype = 'float')
piech_dat = pl.loadtxt('s5_2p9_j3.csv', dtype = 'float')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s5$ ' r'$\rightarrow$'  '$2p9$ ' '($\Delta J=1)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'ro', ms = 2)
pl.plot(10, 2300, 'ro', ms=5)
errorbar = pl.errorbar(10., 2300, yerr=800, linestyle='None',
                       color='red')
pl.show()


#==============================================================================
# %% Cell2
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s5_2p8_J0.dat', dtype = 'float')
piech_dat = pl.loadtxt('s5_2p8_j2.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s5$ ' r'$\rightarrow$'  '$2p8$ ' '($\Delta J=0)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'ro', ms = 2)
#pl.plot(10, 2300, 'ro', ms=5)
#errorbar = pl.errorbar(10., 2300, yerr=800, linestyle='None',
#                       color='red')
pl.show()

#==============================================================================
# %% Cell3
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s5_2p7_J1.dat', dtype = 'float')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s5$ ' r'$\rightarrow$'  '$2p8$ ' '($\Delta J=1)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')

pl.show()

#==============================================================================
# %% Cell4
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s5_2p6_J0.dat', dtype = 'float')
piech_dat = pl.loadtxt('s5_2p6_j2.csv')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s5$ ' r'$\rightarrow$'  '$2p6$ ' '($\Delta J=0)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'ro', ms = 2)

pl.show()

#==============================================================================
# %% Cell5
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s3_2p10_J1.dat', dtype = 'float')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s3$ ' r'$\rightarrow$'  '$2p10$ ' '($\Delta J=1)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')

pl.show()
#==============================================================================
# %% Cell5
#==============================================================================
pl.clf()
brat_dat = pl.loadtxt('1s3_2p9_J3.dat', dtype = 'float')
ax1 = pl.axes()
pl.figure(1, figsize=(8, 6), facecolor='white')
pl.xlabel('Temperature (eV)')
pl.ylabel('Cross section  (MB)')
pl.xlim(0,40)
title = '$1s3$ ' r'$\rightarrow$'  '$2p9$ ' '($\Delta J=3)$'
pl.title(title)
pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')

pl.show()