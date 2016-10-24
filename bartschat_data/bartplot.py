# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:02:57 2016

@author: ivan
"""
import pylab as pl
pl.rcParams['legend.handlelength'] = 0
import os
os.chdir("/home/ivan/Research/brat/piech_data")

def s5_2p10():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p10_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p10.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0,3575])
    label = '1s5' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p10_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p10()

def s5_2p9():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p9_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p9.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,3575])
    label = '1s5' r'$\rightarrow$'  '2p9 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p9_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p9()

def s5_2p8():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p8_J0.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p8.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    label = '1s5' r'$\rightarrow$'  '2p8 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    figname = '1s5-2p8_j0_plot_bart.eps'
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    pl.savefig(figname)
    pl.show()
    return
s5_2p8()

def s5_2p7():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p7_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p7.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0,1350])
    label = '1s5' r'$\rightarrow$'  '2p7 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p7_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p7()

def s5_2p6():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p6_J0.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p6.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,1350])
    label = '1s5' r'$\rightarrow$'  '2p6 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p6_j0_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p6()


def s5_2p5():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p5_J2.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p5.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    label = '1s5' r'$\rightarrow$'  '2p5 ' '($\Delta J=2)$'
    pl.xlim(0,17)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p5_j2_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p5()

def s5_2p4():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p4_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p4.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    label = '1s5' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    pl.xlim(0,17)
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p4_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p4()

def s5_2p3():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p3_J0.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p3.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    label = '1s5' r'$\rightarrow$'  '2p3 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p3_j0_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p3()

def s5_2p2():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p2_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    label = '1s5' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p2_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p2()

def s5_2p1():
    pl.clf()
    brat_dat = pl.loadtxt('1s5_2p1_J2.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s5_2p1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    label = '1s5' r'$\rightarrow$'  '2p1 ' '($\Delta J=2)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    figname = '1s5-2p1_j2_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s5_2p1()

def reject_outliers(data, column, m=2):
    return data[(abs(data[:,column] - pl.mean(data[:,column]))\
     < m * pl.std(data[:,column]))]

def s3_2p10():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p10_J1.dat', dtype = 'float')
    brat_dat = reject_outliers(brat_dat, 1, 2.5)
    brat_dat = reject_outliers(brat_dat, 1, 2.5)
    brat_dat = reject_outliers(brat_dat, 1, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p10.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 1500])
    label = '1s3' r'$\rightarrow$'  '2p10 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0], brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p10_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p10()

def s3_2p9():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p9_J3.dat', dtype = 'float')
    brat_dat = reject_outliers(brat_dat, 1, 2.75)
    brat_dat = reject_outliers(brat_dat, 1, 3.0)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p9.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p9 ' '($\Delta J=3)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r', ms=2)
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p9_j3_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p9()

def s3_2p8():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p8_J2.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p8.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p8 ' '($\Delta J=2)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p8_j2_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p8()


def s3_2p7():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p7_J1.dat', dtype = 'float')
    # brat_dat = reject_outliers(brat_dat, 2, 2)
    # brat_dat = reject_outliers(brat_dat, 2, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p7.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p7 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p7_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p7()

def s3_2p6():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p6_J2.dat', dtype = 'float')
    # brat_dat = reject_outliers(brat_dat, 2, 2)
    # brat_dat = reject_outliers(brat_dat, 2, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p6.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p6 ' '($\Delta J=2)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p6_j2_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p6()

def s3_2p5():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p5_J0.dat', dtype = 'float')
    # brat_dat = reject_outliers(brat_dat, 2, 2)
    # brat_dat = reject_outliers(brat_dat, 2, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p5.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p5 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p5_j0_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p5()

def s3_2p4():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p4_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p4.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,3800])
    label = '1s3' r'$\rightarrow$'  '2p4 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p4_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p4()

def s3_2p3():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p3_J2.dat', dtype = 'float')
    # brat_dat = reject_outliers(brat_dat, 2, 2)
    # brat_dat = reject_outliers(brat_dat, 2, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p3.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p3 ' '($\Delta J=2)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p3_j2_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p3()

def s3_2p2():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p2_J1.dat', dtype = 'float')
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    pl.ylim([0,1900])
    label = '1s3' r'$\rightarrow$'  '2p2 ' '($\Delta J=1)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.legend(loc=1, frameon=False, scatterpoints=0, fontsize=14)
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.plot(bartdat[:,2]-11.548,bartdat[:,3] * 100., 'cD', ms = 7)
    figname = '1s3-2p2_j1_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p2()

def s3_2p1():
    pl.clf()
    brat_dat = pl.loadtxt('1s3_2p1_J0.dat', dtype = 'float')
    # brat_dat = reject_outliers(brat_dat, 2, 2)
    # brat_dat = reject_outliers(brat_dat, 2, 3)
    bartdat = pl.loadtxt('../bartschat_data/paper_figures/s3_2p1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.xlabel('Energy (eV)', fontsize=14)
    pl.ylabel('Cross section  (MB)', fontsize=14)
    pl.xlim(0,17)
    # pl.ylim([0, 500])
    label = '1s3' r'$\rightarrow$'  '2p1 ' '($\Delta J=0)$'
    pl.plot(brat_dat[:,0],brat_dat[:,2], 'b', label = label)
    pl.plot(brat_dat[:,0],brat_dat[:,3], 'g-.')
    pl.plot(brat_dat[:,0],brat_dat[:,1], 'r--')
    pl.plot(bartdat[:,0]-11.548,bartdat[:,1] * 100., 'bo', ms = 7)
    pl.legend(loc=1, markerscale=0, frameon = False, fontsize=14)
    figname = '1s3-2p1_j_plot_bart.eps'
    pl.savefig(figname)
    pl.show()
    return
s3_2p1()
