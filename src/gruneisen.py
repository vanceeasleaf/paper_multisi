# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-23 21:21:33


from aces.tools import exists, shell_exec

from aces.graph import fig, setLegend, pl
import numpy as np
from aces.algorithm.kpoints import filter_along_direction as fad
from aces.io.shengbte import get_qpoints_full as gqf, get_gruneisen, get_omega
from aces.f import binmeanx
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')
import matplotlib
matplotlib.rcParams['ytick.minor.width'] = 1.5
matplotlib.rcParams['ytick.minor.size'] = 3
with fig('gruneisen.eps'):
    fi, axes = pl.subplots(3, 3, sharex=True, sharey=True, figsize=(10, 10))
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
                    dir = "2l1/0/sheng.1/"
                gru = get_gruneisen(dir)
                omega = get_omega(dir)
                qpoints_full, idx = gqf(dir)
                omega_full = omega[idx]
                gru_full = gru[idx]
                dth = np.pi / 10
                if s == "z":
                    phi = 0.0
                else:
                    phi = np.pi / 2.0
                fil = fad(qpoints_full, phi, dth)
                q = np.c_[
                    omega_full[fil].flatten(),
                    gru_full[fil].flatten()]
                q = np.nan_to_num(q)
                x, y = binmeanx(q, [0, 4.49], 0.5)
                mfc = [colors[i], 'w'][s == 'a']
                ls = ['-', '-.'][s == 'a']

                ax.semilogy(x, np.abs(y), ls=ls,
                            marker=markers[i],
                            markersize=9,
                            markeredgecolor=colors[i],
                            markerfacecolor=mfc,
                            color=colors[i],
                            label=v + s)
                ax.set_xlim([0, 4.9])
                setLegend(ax, fontsize=10)
    fi.text(0.5, 0.04, 'Phonon Frequency(THz)', ha='center')
    fi.text(0.05, 0.5, 'Gruneisen Parameter', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
