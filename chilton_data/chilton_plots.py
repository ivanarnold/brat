# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:28:04 2016

@author: ivan
"""

import pylab as pl
import os
%matplotlib inline

def p0_2p10():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p10_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 4.7, 'bs', ms=5)
    pl.plot(20.0, 1.4, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p10 (J=1)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3,   label='2p10 (J=1)')
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p10_J1_plot.eps')
    pl.show()
    return
p0_2p10()

def p0_2p9():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p9_J3.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 5.3, 'bs', ms=5)
    pl.plot(20.0, 3.9, 'bv', ms=5)
    pl.plot(20.0, 2.4, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p9 (J=3)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p9_J3_plot.eps')
    pl.show()
    return
p0_2p9()
# %%>

def p0_2p8():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p8_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 5.4, 'bs', ms=5)
    pl.plot(20.0, 2.4, 'bv', ms=5)
    pl.plot(20.0, 1.3, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p8 (J=2)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p8_J2_plot.eps')
    pl.show()
    return
p0_2p8()

def p0_2p7():
    pl.clf()
    ax1 = pl.axes()
    ourdat  = pl.loadtxt('1p0_2p7_J1.dat')
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 2.5, 'bs', ms=5)
    pl.plot(20.0, 1.9, 'bv', ms=5)
    pl.plot(20.0, 1.4, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p7 (J=1)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p7_J1_plot.eps')
    pl.show()
    return
p0_2p7()


def p0_2p6():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p6_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 3.2, 'bs', ms=5)
    pl.plot(20.0, 1.7, 'bv', ms=5)
    pl.plot(20.0, 1.5, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p6 (J=2)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p6_J2_plot.eps')
    pl.show()
    return
p0_2p6()


def p0_2p5():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p5_J0.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 1.6, 'bs', ms=5)
    pl.plot(20.0, 1.6, 'bv', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p5 (J=0)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=4)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p5_J0_plot.eps')
    pl.show()
    return
p0_2p5()

def p0_2p4():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p4_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 2.2, 'bs', ms=5)
    pl.plot(20.0, 1.7, 'bv', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p4 (J=1)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p4_J1_plot.eps')
    pl.show()
    return
p0_2p4()


def p0_2p3():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p3_J2.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 2.9, 'bs', ms=5)
    pl.plot(20.0, 3.7, 'bv', ms=5)
    pl.plot(20.0, 1.1, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p3 (J=2)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=1)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p3_J2_plot.eps')
    pl.show()
    return
p0_2p3()

def p0_2p2():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p2_J1.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 1.4, 'bs', ms=5)
    pl.plot(20.0, 1.8, 'bv', ms=5)
    pl.plot(20.0, 0.58, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p2 (J=1)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=2)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p2_J1_plot.eps')
    pl.show()
    return
p0_2p2()


def p0_2p1():
    pl.clf()
    ourdat  = pl.loadtxt('1p0_2p1_J0.dat')
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    pl.plot(20.0, 5.0, 'bs', ms=5)
    pl.plot(20.0, 5.2, 'bv', ms=5)
    pl.plot(20.0, 2.7, 'bo', ms=5)
    pl.plot(ourdat[:,0], ourdat[:,1], 'r', ms=3,  label='2p1 (J=0)')
    pl.plot(ourdat[:,0], ourdat[:,2], 'b--', ms=3)
    pl.plot(ourdat[:,0], ourdat[:,3], 'g-.', ms=3)
    pl.legend(loc=2)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig('1p0-2p1_J0_plot.eps')
    pl.show()
    return
p0_2p1()


def excfunc():
    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    ourdat9  = pl.loadtxt('1p0_2p9_J3.dat')
    chil_dir9 = pl.loadtxt('chilton_2p9.dat')
    pl.plot(ourdat9[:,0], ourdat9[:,2], 'r', ms=3, label='2p9 (J=3)')
    pl.plot(chil_dir9[:,0], chil_dir9[:,1] / 10. *0.5, 'ro', ms=5)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig("2p9_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    ourdat8  = pl.loadtxt('1p0_2p8_J2.dat')
    chil_dir8 = pl.loadtxt('chilton_2p8.dat')
    pl.plot(ourdat8[:,0], ourdat8[:,2], 'g.-', ms=3, label='2p8 (J=2)')
    pl.plot(chil_dir8[:,0], chil_dir8[:,1] / 10. *0.55, 'gs', ms=5)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig("2p8_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir7 = pl.loadtxt('chilton_2p7.dat')
    ourdat7  = pl.loadtxt('1p0_2p7_J1.dat')
    pl.plot(ourdat7[:,0], ourdat7[:,2], 'b--', ms=3,  label='2p7 (J=1)')
    pl.plot(chil_dir7[:,0], chil_dir7[:,1] / 10. *0.5, 'bs', ms=5)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig("2p7_excit.eps")
    pl.show()

    pl.clf()
    ax1 = pl.axes()
    pl.figure(1, figsize=(8, 6), facecolor='white')
    chil_dir5 = pl.loadtxt('chilton_2p5.dat')
    ourdat5  = pl.loadtxt('1p0_2p5_J0.dat')
    pl.plot(ourdat5[:,0], ourdat5[:,2], 'k-', ms=3,  label='2p5 (J=0)')
    pl.plot(chil_dir5[:,0], chil_dir5[:,1] / 10. *0.8, 'ks', ms=5)
    pl.xlim([10,35])
    pl.ylim(ymin=0.0)
    pl.savefig("2p5_excit.eps")
    pl.show()

    return
excfunc()
