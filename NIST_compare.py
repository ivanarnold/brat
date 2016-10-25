# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 06:32:12 2016

@author: ivan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:02:57 2016

@author: ivan
"""
#%%
import pylab as pl
pl.rcParams['legend.handlelength'] = 0
import os
os.chdir("C:\\Users\\ivan\\Research\\brat\\piech_data\\newNIST")
#%%
def s5_2p9():
    pl.clf()
    brat_dat = pl.loadtxt('../1s5_2p9_J1.dat', dtype = 'float')
    old_brat_dat = pl.loadtxt('1s5_2p9_J1.dat', dtype = 'float')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,3575])
    label = '1s5' r'$\rightarrow$'  '2p9 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,2], 'b.', ms=3)
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,3], 'g.', ms=3)
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,1], 'r.', ms=3)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p9_j1_NISTcomp.png'
    pl.savefig(figname)
    pl.show()
    return
s5_2p9()
#%%
def s5_2p6():
    pl.clf()
    brat_dat = pl.loadtxt('../1s5_2p6_J0.dat', dtype = 'float')
    old_brat_dat = pl.loadtxt('1s5_2p6_J0.dat', dtype = 'float')
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,1350])
    label = '1s5' r'$\rightarrow$'  '2p6 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r')
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,2], 'b.', ms=3)
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,3], 'g.', ms=3)
    pl.plot(old_brat_dat[::3,0],old_brat_dat[::3,1], 'r.', ms=3)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p6_j0_NISTcomp.png'
    pl.savefig(figname)
    pl.show()
    return
s5_2p6()