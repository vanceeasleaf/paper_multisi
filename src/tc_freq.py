# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-10-28 15:40:24


from aces.graph import fig, setLegend, pl
import numpy as np
from aces.algorithm.kpoints import filter_along_direction as fad
from aces.io.shengbte import get_qpoints_full as gqf, get_tau, get_omega
from aces.f import binmeanx
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')
import matplotlib
matplotlib.rcParams['ytick.minor.width'] = 1.5
matplotlib.rcParams['ytick.minor.size'] = 3
with fig('tc_freq.eps'):
    fi, axes = pl.subplots(2, 3, sharex=True, sharey=True, figsize=(10, 6))
    for j in range(2):
        if j == 0:
            vs = "2l1,2lhex,3l1".split(',')
        if j == 1:
            vs = "4l1,5l1,6l1".split(',')
        for i, v in enumerate(vs):
            for s in ['z', 'a']:
                ax = axes[j, i]
                dir = "%s/0/SHENG" % v
                if v == "2l1":
                    dir = "2l1/0/sheng.1"
                kappa = np.loadtxt(
                    dir + '/T300K/BTE.cumulative_kappaVsOmega_tensor')
                df = kappa[2, 0] - kappa[0, 0]
                p = np.arange(len(kappa) - 2)
                mfc = [colors[0], 'w'][s == 'a']
                ls = ['-', '-.'][s == 'a']
                if s == "z":
                    ax.plot(
                        kappa[p, 0],
                        (kappa[p + 2, 1] - kappa[p, 1]) / df,
                        label=v + s, ls=ls,
                        marker=markers[0],
                        markersize=9,
                        markeredgecolor=colors[0],
                        markerfacecolor=mfc,
                        color=colors[0])
                else:
                    ax.plot(
                        kappa[p, 0],
                        (kappa[p + 2, 5] - kappa[p, 5]) / df,
                        label=v + s, ls=ls,
                        marker=markers[0],
                        markersize=9,
                        markeredgecolor=colors[0],
                        markerfacecolor=mfc,
                        color=colors[0])

                ax.set_xlim([0, 20.55])
                ax.set_ylim([0, 1])
                # ax.set_yticks([])
                setLegend(ax, fontsize=10)
    fi.text(0.5, 0.04, 'Phonon Frequency (THz)', ha='center')
    fi.text(
        0.05,
        0.5,
        'Thermal Conductivity (W/mK)',
        va='center',
        rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
