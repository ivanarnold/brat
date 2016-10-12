# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:02:57 2016

@author: ivan
"""
import pylab as pl
pl.rcParams['legend.handlelength'] = 0
import os
os.chdir("/home/ivan/Research/brat/piech_data")

# def s5_2p10():
#     pl.clf()
#     brat_dat = pl.loadtxt('1s5_2p10_J1.dat', dtype = 'float')
#     ax1 = pl.axes()
#     pl.figure(1, figsize=(8, 6), facecolor='white')
#     pl.xlabel('Temperature (eV)')
#     pl.ylabel('Cross section  (MB)')
#     pl.xlim(0,20)
#     pl.ylim([0,1450])
#     label = '1s5' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
#     pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
#     pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
#     pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
#     pl.legend(loc=1, frameon=False, scatterpoints=0)
#     figname = '1s5-2p10_j1_plot.eps'
#     pl.savefig(figname)
#     pl.show()
#     return
# s5_2p10()

def s5_2p9():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p9_J1.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p9_j3.csv', dtype = 'float')
    bartdat = pl.genfromtxt('../bartschat_data/paper_figures/piech_2p9s5.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    # pl.xlim(0,20)
    pl.ylim([0,3575])
    label = '1s5' r'$\rightarrow$'  '2p9 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2] + 1.0 * brat_dat[:,3], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0], 1.0 * brat_dat[:,3], 'g--')
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'rs', ms = 4)
    # pl.plot(bartdat[:,0],bartdat[:,1] * 100., 'rs', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    figname = '1s5-2p9_j1_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p9()

def s5_2p8():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p8_J0.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p8_j2.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p8.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    label = '1s5' r'$\rightarrow$'  '2p8 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2] + 1.0 * brat_dat[:,3], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0], 1.0 *brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'rs', ms = 4)
    figname = '1s5-2p8_j0_plot.eps'
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.savefig(figname)
    pl.show()
    return
s5_2p8()

# def s5_2p7():
#     pl.clf()
#     brat_dat = pl.loadtxt('1s5_2p7_J1.dat', dtype = 'float')
#     #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p7.txt')
#     ax1 = pl.axes()
#     pl.figure(1, figsize=(8, 6), facecolor='white')
#     pl.xlabel('Temperature (eV)')
#     pl.ylabel('Cross section  (MB)')
#     pl.xlim(0,20)
#     label = '1s5' r'$\rightarrow$'  '2p7 ' '($\Delta J=1)$'
#     pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
#     pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
#     pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
#     #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
#     pl.legend(loc=1, frameon=False, scatterpoints=0)
#     figname = '1s5-2p7_j1_plot.eps'
#     pl.savefig(figname)
#     pl.show()
#     return
# s5_2p7()

def s5_2p6():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p6_J0.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p6_j2.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p6.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    pl.ylim([0,1350])
    label = '1s5' r'$\rightarrow$'  '2p6 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2] + 1.0 * brat_dat[:,3], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0], 1.0 * brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100. , 'rs', ms = 4)
    figname = '1s5-2p6_j0_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p6()


def s5_2p5():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p5_J2.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p5_j0.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p5.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    label = '1s5' r'$\rightarrow$'  '2p5 ' '($\Delta J=2)$'
    pl.xlim(0,20)
    pl.plot(brat_dat[:,0],brat_dat[:,2] + 1.0 * brat_dat[:,3], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0], 1.0 * brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'rs', ms = 5)
    figname = '1s5-2p5_j2_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p5()

def s5_2p4():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p4_J1.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p4_j1.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p4.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    label = '1s5' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    pl.xlim(0,20)
    pl.plot(brat_dat[:,0],brat_dat[:,2] + 1.0 * brat_dat[:,3], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0], 1.0 * brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100. * 1., 'rs', ms = 5)
    figname = '1s5-2p4_j1_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p4()

def s5_2p3():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p3_J0.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p3_j2.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p3.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    label = '1s5' r'$\rightarrow$'  '2p3 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100., 'rs', ms = 4)
    figname = '1s5-2p3_j0_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p3()

def s5_2p2():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p2_J1.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s5_2p2_j1.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p2.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    label = '1s5' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100. , 'rs', ms = 4)
    figname = '1s5-2p2_j1_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p2()

def s3_2p4():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p4_J1.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s3_2p4_j1.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p4.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    pl.ylim([0,3800])
    label = '1s3' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    pl.legend(loc=1, markerscale=0, frameon = False)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100. , 'rs', ms = 4)
    figname = '1s3-2p4_j1_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p4()

def s3_2p2():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p2_J1.dat', dtype = 'float')
    piech_dat = pl.loadtxt('s3_2p2_j1.csv')
    #bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p2.txt')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Temperature (eV)')
    pl.ylabel('Cross section  (MB)')
    pl.xlim(0,20)
    pl.ylim([0,1800])
    label = '1s3' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
    pl.legend(loc=1, frameon=False, scatterpoints=0)
    pl.plot(piech_dat[:,0],piech_dat[:,1] * 100. * 1.4, 'rs', ms = 4)
    #pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 4)
    figname = '1s3-2p2_j1_plot.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p2()

# def s3_2p10():
#     pl.clf()
#     brat_dat = pl.loadtxt('1s3_2p10_J1.dat', dtype = 'float')
#     ax1 = pl.axes()
#     pl.figure(1, figsize=(8, 6), facecolor='white')
#     pl.xlabel('Temperature (eV)')
#     pl.ylabel('Cross section  (MB)')
#     pl.xlim(0,20)
#     label = '1s5' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
#     pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
#     pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
#     pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
#     pl.legend(loc=1, frameon=False, scatterpoints=0)
#     figname = '1s3-2p10_j1_plot.eps'
#     pl.savefig(figname)
#     pl.show()
#     return
# s3_2p10()
#
# def s3_2p9():
#     pl.clf()
#     brat_dat = pl.loadtxt('1s3_2p9_J3.dat', dtype = 'float')
#     ax1 = pl.axes()
#     pl.figure(1, figsize=(8, 6), facecolor='white')
#     pl.xlabel('Temperature (eV)')
#     pl.ylabel('Cross section  (MB)')
#     pl.xlim(0,40)
#     pl.xlim(0,20)
#     label = '1s3' r'$\rightarrow$'  '2p9 ' '($\Delta J=3)$'
#     pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', label=label)
#     pl.plot(brat_dat[:,0],brat_dat[:,2], 'b-.')
#     pl.plot(brat_dat[:,0],brat_dat[:,3], 'g--')
#     pl.legend(loc=1, frameon=False, scatterpoints=0)
#     figname = '1s3-2p9_j3_plot.eps'
#     pl.savefig(figname)
#     pl.show()
#     return
# s3_2p9()
