# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-08-11 11:01:28


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
    fi, axes = pl.subplots(3, 3, sharex=True, sharey=False, figsize=(10, 10))
    for j in range(3):
        if j == 0:
            vs = "2l1,2l2,2lhex".split(',')
        if j == 1:
            vs = "3l1,3l2,4l1".split(',')
        if j == 2:
            vs = "5l1,6l1,Silicene".split(',')
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
                if s == "z":
                    ax.plot(
                        kappa[p, 0],
                        (kappa[p + 2, 1] - kappa[p, 1]) / df,
                        label=v + s)
                else:
                    ax.plot(
                        kappa[p, 0],
                        (kappa[p + 2, 5] - kappa[p, 5]) / df,
                        label=v + s)

                ax.set_xlim([0, 20.55])
                ax.set_ylim([0, None])
                ax.set_yticks([])
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
