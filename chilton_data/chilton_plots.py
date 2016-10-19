# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:28:04 2016

@author: ivan
"""

import pylab as pl
pl.rcParams['legend.handlelength'] = 0
import os
from scipy.ndimage.filters import gaussian_filter

os.chdir('/home/ivan/Research/brat/chilton_data')

def p0_1s5():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_1s5_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 4.7, 'gs', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '1s5 ' '($\Delta J=2)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_1s5.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1], 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3], 'mp', ms=9, lw=5) #Khakoo
    pl.plot(zatsdat[:,4], zatsdat[:,5], 'gs', ms=7, lw=5) #Filopivic
    pl.plot(zatsdat[:,6], zatsdat[:,7], 'cD', ms=7, lw=5) #Chutjian
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,35])
    pl.ylim([0,10])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-1s5_J2_plot.eps')
    pl.show()
    return
p0_1s5()
# zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
# print(zatsdat)

def p0_1s4():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_1s4_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 4.7, 'gs', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '1s4 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_1s4.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1], 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3], 'y*', ms=9, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5], 'mp', ms=7, lw=5)
    pl.plot(zatsdat[:,6], zatsdat[:,7], 'gs', ms=7, lw=5)
    pl.plot(zatsdat[:,8], zatsdat[:,9], 'cD', ms=9, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,35])
    # pl.ylim([0,5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-1s4_J1_plot.eps')
    pl.show()
    return
p0_1s4()

def p0_1s3():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_1s3_J0.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 4.7, 'gs', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '1s3 ' '($\Delta J=0)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_1s3.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1], 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3], 'mp', ms=9, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5], 'gs', ms=7, lw=5)
    pl.plot(zatsdat[:,6], zatsdat[:,7], 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,35])
    # pl.ylim([0,5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-1s3_J0_plot.eps')
    pl.show()
    return
p0_1s3()

def p0_1s2():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_1s2_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 4.7, 'gs', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '1s2 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_1s2.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1], 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3], 'y*', ms=9, lw=5) # Hoshino
    pl.plot(zatsdat[:,4], zatsdat[:,5], 'mp', ms=7, lw=5) # Khakoo
    pl.plot(zatsdat[:,6], zatsdat[:,7], 'gs', ms=7, lw=5) # Filopivic
    pl.plot(zatsdat[:,8], zatsdat[:,9], 'cD', ms=9, lw=5) # Chutjian
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,35])
    # pl.ylim([0,5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-1s2_J1_plot.eps')
    pl.show()
    return
p0_1s2()

def p0_2p10():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p10_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 4.7, 'gs', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'gs', ms=7, lw=5)
    pl.plot(zatsdat[:,6], zatsdat[:,7]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim([0,5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p10_J1_plot.eps')
    pl.show()
    return
p0_2p10()
# zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
# print(zatsdat)
def p0_2p9():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p9_J3.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 5.3, 'gs', ms=7)
    # pl.plot(20.0, 3.9, 'bv', ms=7)
    # pl.plot(20.0, 2.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p9 ' '($\Delta J=3)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p9.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim(ymin=0.0)
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p9_J3_plot.eps')
    pl.show()
    return
p0_2p9()

# zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
# print(zatsdat)

def p0_2p8():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p8_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 5.4, 'gs', ms=7)
    # pl.plot(20.0, 2.4, 'bv', ms=7)
    # pl.plot(20.0, 1.3, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p8 ' '($\Delta J=2)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p8.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim(ymin=0.0)
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p8_J2_plot.eps')
    pl.show()
    return
p0_2p8()

# zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
# print(zatsdat)

def p0_2p7():
    pl.clf()
    ax1 = pl.axes()
    ourdat  = pl.loadtxt('1p0_2p7_J1.dat')
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 2.5, 'gs', ms=7)
    # pl.plot(20.0, 1.9, 'bv', ms=7)
    # pl.plot(20.0, 1.4, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p7 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p7.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim(ymin=0.0, ymax=3.0)
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p7_J1_plot.eps')
    pl.show()
    return
p0_2p7()

# zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
# print(zatsdat)

def p0_2p6():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p6_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 3.2, 'gs', ms=7)
    # pl.plot(20.0, 1.7, 'bv', ms=7)
    # pl.plot(20.0, 1.5, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p6 ' '($\Delta J=2)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    # pl.plot(ourdat[:,0], gaussian_filter(ourdat[:,2], sigma=10), \
    #         'b', ms=7, label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p6.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim([0.0,3.5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p6_J2_plot.eps')
    pl.show()
    return
p0_2p6()

def p0_2p5():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p5_J0.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 1.6, 'gs', ms=7)
    # pl.plot(20.0, 1.6, 'bv', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p5 ' '($\Delta J=0)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p5.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'gs', ms=7, lw=5)
    pl.plot(zatsdat[:,6], zatsdat[:,7]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim(ymin=0.0)
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p5_J0_plot.eps')
    pl.show()
    return
p0_2p5()

def p0_2p4():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p4_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 2.2, 'gs', ms=7)
    # pl.plot(20.0, 1.7, 'bv', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p10.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim(ymin=0.0)
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p4_J1_plot.eps')
    pl.show()
    return
p0_2p4()

def p0_2p3():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p3_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 2.9, 'gs', ms=7)
    # pl.plot(20.0, 3.7, 'bv', ms=7)
    # pl.plot(20.0, 1.1, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p3 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p3.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim([0,3.7])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p3_J2_plot.eps')
    pl.show()
    return
p0_2p3()

def p0_2p2():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p2_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 1.4, 'gs', ms=7)
    # pl.plot(20.0, 1.8, 'bv', ms=7)
    # pl.plot(20.0, 0.58, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p2.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim([0,1.7])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p2_J1_plot.eps')
    pl.show()
    return
p0_2p2()

def p0_2p1():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p1_J0.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    # pl.plot(20.0, 5.0, 'gs', ms=7)
    # pl.plot(20.0, 5.2, 'bv', ms=7)
    # pl.plot(20.0, 2.7, 'bo', ms=7)
    label = '1p0' r'$\rightarrow$'  '2p1 ' '($\Delta J=0)$'
    # pl.plot(ourdat[:,0], ourdat[:,1], 'r--', ms=7,  label=label)
    pl.plot(ourdat[:,0], ourdat[:,2], 'b', ms=7, label=label)
    # pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=7)
    zatsdat = pl.loadtxt('../zats_figs/zats_2p1.dat')
    pl.plot(zatsdat[:,0], zatsdat[:,1]/10, 'ro',)
    pl.plot(zatsdat[:,2], zatsdat[:,3]/10, 'k^', ms=7, lw=5)
    pl.plot(zatsdat[:,4], zatsdat[:,5]/10, 'gs', ms=7, lw=5)
    pl.plot(zatsdat[:,6], zatsdat[:,7]/10, 'cD', ms=7, lw=5)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.xlim([12,42])
    pl.ylim([0,15])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.savefig('1p0-2p1_J0_plot.eps')
    pl.show()
    return
p0_2p1()

def excfunc():

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    ourdat10  = pl.loadtxt('1p0_2p10_J1.dat')
    chil_dir10 = pl.loadtxt('chilton_2p10.dat')
    label = '1p0' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
    pl.plot(ourdat10[:,0], ourdat10[:,2], 'b', label=label)
    pl.plot(ourdat10[:,0], ourdat10[:,3], 'g-.')
    pl.plot(chil_dir10[:,0], chil_dir10[:,1] / 10. *0.7, 'bo')
    pl.plot(chil_dir10[:,2], chil_dir10[:,3] / 10. * 0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir9[:,0], chil_dir9[:,1] / 10. *0.5 , \
    #            yerr = chil_dir9[:,1] / 10. *0.5 *0.35, linestyle='None', \
    #            color='red')
    pl.xlim([10,42])
    pl.ylim([0,8.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p10_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    ourdat9  = pl.loadtxt('1p0_2p9_J3.dat')
    chil_dir9 = pl.loadtxt('chilton_2p9.dat')
    label = '1p0' r'$\rightarrow$'  '2p9 ' '($\Delta J=3)$'
    pl.plot(ourdat9[:,0], ourdat9[:,2], 'b', ms=7, label=label)
    pl.plot(ourdat9[:,0], ourdat9[:,3], 'g-.')
    pl.plot(chil_dir9[:,0], chil_dir9[:,1] / 10., 'bo')
    pl.plot(chil_dir9[:,2], chil_dir9[:,3] / 10., 'gD')
    # errorbar = pl.errorbar(chil_dir9[:,0], chil_dir9[:,1] / 10. *0.5 , \
    #            yerr = chil_dir9[:,1] / 10. *0.5 *0.35, linestyle='None', \
    #            color='red')
    pl.xlim([12,42])
    # pl.ylim([0,4.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p9_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    ourdat8  = pl.loadtxt('1p0_2p8_J2.dat')
    chil_dir8 = pl.loadtxt('chilton_2p8.dat')
    label = '1p0' r'$\rightarrow$'  '2p8 ' '($\Delta J=2)$'
    pl.plot(ourdat8[:,0], ourdat8[:,2], 'b', label=label)
    pl.plot(ourdat8[:,0], ourdat8[:,3], 'g-.')
    pl.plot(chil_dir8[:,0], chil_dir8[:,1] / 10. * 0.7, 'bo')
    pl.plot(chil_dir8[:,2], chil_dir8[:,3] / 10. * 0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir8[:,0], chil_dir8[:,1] / 10. *0.7 , \
    #            yerr = chil_dir8[:,1] / 10. *0.7 *0.35, linestyle='None', \
    #            color='red')
    pl.xlim([12,42])
    # pl.ylim([0,4.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p8_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir7 = pl.loadtxt('chilton_2p7.dat')
    ourdat7  = pl.loadtxt('1p0_2p7_J1.dat')
    label = '1p0' r'$\rightarrow$'  '2p7 ' '($\Delta J=1)$'
    pl.plot(ourdat7[:,0], ourdat7[:,2], 'b', label=label)
    pl.plot(ourdat7[:,0], ourdat7[:,3], 'g-.')
    pl.plot(chil_dir7[:,0], chil_dir7[:,1] / 10. * 0.6, 'bo')
    pl.plot(chil_dir7[:,2], chil_dir7[:,3] / 10. * 0.6, 'gD')
    # errorbar = pl.errorbar(chil_dir7[:,0], chil_dir7[:,1] / 10. *0.6 , \
    #            yerr = chil_dir7[:,1] / 10. *0.6 *0.35, linestyle='None', \
    #            color='red')
    pl.xlim([12,42])
    # pl.ylim([0,2.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p7_excit.eps")
    pl.show()


    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir6 = pl.loadtxt('chilton_2p6.dat')
    ourdat6  = pl.loadtxt('1p0_2p6_J2.dat')
    label = '1p0' r'$\rightarrow$'  '2p6 ' '($\Delta J=2)$'
    pl.plot(ourdat6[:,0], ourdat6[:,2], 'b', label=label)
    pl.plot(ourdat6[:,0], ourdat6[:,3], 'g-.')
    pl.plot(chil_dir6[:,0], chil_dir6[:,1] / 10. * 0.7, 'bo')
    pl.plot(chil_dir6[:,2], chil_dir6[:,3] / 10. *0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir7[:,0], chil_dir7[:,1] / 10. *0.5 , \
    #            yerr = chil_dir7[:,1] / 10. *0.5 *0.35, linestyle='None', \
    #            color='blue')
    pl.xlim([12,42])
    # pl.ylim([0,2.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p6_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir5 = pl.loadtxt('chilton_2p5.dat')
    ourdat5  = pl.loadtxt('1p0_2p5_J0.dat')
    label = '1p0' r'$\rightarrow$'  '2p5 ' '($\Delta J=0)$'
    pl.plot(ourdat5[:,0], ourdat5[:,2], 'b', label=label)
    pl.plot(ourdat5[:,0], ourdat5[:,3], 'g-.')
    pl.plot(chil_dir5[:,0], chil_dir5[:,1] / 10. * 0.7, 'bo')
    pl.plot(chil_dir5[:,2], chil_dir5[:,3] / 10. * 0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8 , \
    #            yerr = chil_dir5[:,1] / 10. *0.8 *0.35, linestyle='None', \
    #            color='black')
    pl.xlim([12,42])
    pl.ylim([0,2.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p5_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir4 = pl.loadtxt('chilton_2p4.dat')
    ourdat4  = pl.loadtxt('1p0_2p4_J1.dat')
    label = '1p0' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    pl.plot(ourdat4[:,0], ourdat4[:,2], 'b', label=label)
    pl.plot(ourdat4[:,0], ourdat4[:,3], 'g-.')
    pl.plot(chil_dir4[:,0], chil_dir4[:,1] / 10. * 0.7, 'bo')
    pl.plot(chil_dir4[:,2], chil_dir4[:,3] / 10. * 0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8 , \
    #            yerr = chil_dir5[:,1] / 10. *0.8 *0.35, linestyle='None', \
    #            color='black')
    pl.xlim([12,42])
    # pl.ylim([0,2.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p4_excit.eps")
    pl.show()


    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir3 = pl.loadtxt('chilton_2p3.dat')
    ourdat3 = pl.loadtxt('1p0_2p3_J2.dat')
    label = '1p0' r'$\rightarrow$'  '2p3 ' '($\Delta J=2)$'
    pl.plot(ourdat3[:,0], ourdat3[:,2], 'b', label=label)
    pl.plot(ourdat3[:,0], ourdat3[:,3], 'g-.')
    pl.plot(chil_dir3[:,0], chil_dir3[:,1] / 10. *0.7, 'bo')
    pl.plot(chil_dir3[:,2], chil_dir3[:,3] / 10. *0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8 , \
    #            yerr = chil_dir5[:,1] / 10. *0.8 *0.5, linestyle='None', \
    #            color='black')
    pl.xlim([12,42])
    # pl.ylim([0,2.0])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p3_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir2 = pl.loadtxt('chilton_2p2.dat')
    ourdat2 = pl.loadtxt('1p0_2p2_J1.dat')
    label = '1p0' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    pl.plot(ourdat2[:,0], ourdat2[:,2], 'b', label=label)
    pl.plot(ourdat2[:,0], ourdat2[:,3], 'g-.')
    pl.plot(chil_dir2[:,0], chil_dir2[:,1] / 10. *0.5, 'bo')
    pl.plot(chil_dir2[:,2], chil_dir2[:,3] / 10. *0.5 , 'gD')
    # errorbar = pl.errorbar(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8 , \
    #            yerr = chil_dir5[:,1] / 10. *0.8 *0.5, linestyle='None', \
    #            color='black')
    pl.xlim([12,42])
    pl.ylim([0,1.5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p2_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir1 = pl.loadtxt('chilton_2p1.dat')
    ourdat1 = pl.loadtxt('1p0_2p1_J0.dat')
    label = '1p0' r'$\rightarrow$'  '2p1 ' '($\Delta J=0)$'
    pl.plot(ourdat1[:,0], ourdat1[:,2], 'b', label=label)
    pl.plot(ourdat1[:,0], ourdat1[:,3], 'g-.')
    pl.plot(chil_dir1[:,0], chil_dir1[:,1] / 10. *0.7, 'bo')
    pl.plot(chil_dir1[:,2], chil_dir1[:,3] / 10. *0.7, 'gD')
    # errorbar = pl.errorbar(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8 , \
    #            yerr = chil_dir5[:,1] / 10. *0.8 *0.5, linestyle='None', \
    #            color='black')
    pl.xlim([12,42])
    # pl.ylim([0,1.5])
    pl.xlabel('Energy (eV)', fontsize=16)
    pl.ylabel('Cross section (MB)', fontsize=16)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig("2p2_excit.eps")
    pl.show()

    return
excfunc()
