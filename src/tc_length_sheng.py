# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-14 22:16:16
# @Last Modified by:   YangZhou
# @Last Modified time: 2018-01-09 17:01:27
from aces.tools import *
from aces.graph import fig, setLegend, pl, fit
import numpy as np

from ase import io


def ff(p, x):
    return p[0] * (1.0 - np.exp(-x / p[1]))
    # return 1.0/(p[1]/x+1/p[0])-p[2]
    # return p[0]*p[1]**x
kas = []
with fig('tc_length_sheng.eps', figsize=(7, 8)):
    markers = ['s', '8', '^', 'D', '>']
    colors = "k,r,b,purple,g".split(',')
    vs = '2l1,2l2,2lhex'.split(',')
    text_style = dict(horizontalalignment='left', verticalalignment='center',
                      fontsize=14, fontdict={'family': 'serif'})
    fi, axes = pl.subplots(2, 1, sharex=True, figsize=(7, 8))
    ax1 = axes[0]
    for s in ['z', 'a']:
        for i, v in enumerate(vs):
            dir = "%s/0/SHENG" % v
            if v == "2l1":
                dir = "2l1/0/sheng.1"
            kappa = np.loadtxt(
                dir + '/T300K/BTE.cumulative_kappa_tensor')[::3]
            m = markers[i]
            c = colors[i]

            l = kappa[:, 0]
            atoms = io.read(v + "/0/secondorder/POSCAR")
            if v == 'Silicene':
                nlayer = 1
            else:
                nlayer = int(v.split('l')[0])
            ss = np.linalg.norm(atoms.cell[2]) / (
                3.34 * nlayer)

            z = kappa[:, 1] * ss
            a = kappa[:, 5] * ss
            if s == 'z':
                opts = dict(
                    markeredgecolor='w',
                    marker=m,
                    color=c,
                    markersize=8 + 2,
                    ls='.')
                o1 = "-"
                ka = z
            else:
                opts = dict(
                    markeredgecolor=c,
                    marker=m,
                    color='w',
                    markersize=8,
                    ls='.')
                o1 = "--"
                ka = a
            if v == '2lhex':
                v = '2l3'
            label = v + s
            kas.append(ka[-1])
            ax1.semilogx(l, ka, label=label, **opts)
            p = fit(l, ka, [1, 1, 1], ff)
            xx = np.linspace(10, 1e4, 1000)
            ax1.semilogx(xx, ff(p, xx), color=c, ls=o1)
            ax1.set_ylabel("Thermal Conductivity(W/mK)")
            # ax1.set_xticks([])
            ax1.set_ylim([-3, 60])
            ax1.text(-.15, 1, 'a)', transform=ax1.transAxes, **text_style)

    kas = np.array(kas).reshape([2, -1])
    for i, v in enumerate(vs):
        kai = np.abs(kas[0][ i] - kas[1][i ]) / \
            np.max([kas[0][i], kas[1][i]]) * 100
        print(v + "z=" + str(kas[0][i]) + " " + v +
              "a=" + str(kas[1][i]) + " kai=" + str(kai) + "%")
    kas = []
    setLegend(ax1, ncol=1, loc=0, fontsize=12)
    ax1 = axes[1]
    vs = '3l1,4l1,5l1,6l1,8l1'.split(',')
    for s in ['z', 'a']:
        for i, v in enumerate(vs):

            dir = "%s/0/SHENG" % v
            if v == "2l1":
                dir = "2l1/0/sheng.1"
            kappa = np.loadtxt(
                dir + '/T300K/BTE.cumulative_kappa_tensor')[::3]
            m = markers[i]
            c = colors[i]
            l = kappa[:, 0]
            atoms = io.read(v + "/0/secondorder/POSCAR")
            nlayer = int(v.split('l')[0])
            ss = np.linalg.norm(atoms.cell[2]) / (
                3.34 * nlayer)

            z = kappa[:, 1] * ss
            a = kappa[:, 5] * ss
            if s == 'z':
                opts = dict(
                    markeredgecolor='w',
                    marker=m,
                    color=c,
                    markersize=8 + 2,
                    ls='.')
                o1 = "-"
                ka = z
            else:
                opts = dict(
                    markeredgecolor=c,
                    marker=m,
                    color='w',
                    markersize=8,
                    ls='.')
                o1 = "--"
                ka = a
            label = v + s
            kas.append(ka[-1])
            ax1.semilogx(l, ka, label=label, **opts)
            p = fit(l, ka, [1, 1, 1], ff)
            xx = np.linspace(10, 1e4, 1000)
            ax1.semilogx(xx, ff(p, xx), color=c, ls=o1)
            ax1.set_xlabel(
                "Cutoff Mean Free Path for Phonons (${ \\AA }$)")
            ax1.set_ylim([-2, 39])
            ax1.set_xlim([0.5, 1e5])
            ax1.set_ylabel("Thermal Conductivity(W/mK)")
            ax1.text(-.15, 1, 'b)', transform=ax1.transAxes, **text_style)
    setLegend(ax1, ncol=1, loc=0, fontsize=12)
    kas = np.array(kas).reshape([2, -1])
    for i, v in enumerate(vs):
        kai = np.abs(kas[0][ i] - kas[1][i ]) / \
            np.max([kas[0][i], kas[1][i]]) * 100
        print(v + "z=" + str(kas[0][i]) + " " + v +
              "a=" + str(kas[1][i]) + " kai=" + str(kai) + "%")
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
