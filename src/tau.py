# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-12-16 16:04:01


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
with fig('tau.eps'):
    fi, axes = pl.subplots(2, 3, sharex=True, sharey=True, figsize=(8, 5))
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
                qpoints_full, idx = gqf(dir)
                omega = get_omega(dir)
                tau = get_tau(dir)
                tau_full = tau[idx]
                omega_full = omega[idx]
                dth = np.pi / 10

                if s == "z":
                    phi = 0.0
                else:
                    phi = np.pi / 2.0
                fil = fad(qpoints_full, phi, dth)
                q = np.c_[
                    omega_full[fil].flatten(),
                    tau_full[fil].flatten()]
                q = np.nan_to_num(q)

                x, y = binmeanx(q, [0.0, 20.0], dx=1.5)
                mfc = [colors[i], 'w'][s == 'a']
                ls = ['-', '-.'][s == 'a']
                v1 = v
                if v1 == '2lhex':
                    v1 = '2l3'
                ax.semilogy(
                    x,
                    y,
                    ls=ls,
                    marker=markers[i],
                    markersize=9,
                    markeredgecolor=colors[i],
                    markerfacecolor=mfc,
                    color=colors[i],
                    label=v1 + s)
                ax.axhline(
                    y=1,
                    xmin=0,
                    xmax=20.55,
                    linewidth=1,
                    color='k',
                    ls='--')
                ax.set_xlim([0.01, 19.55])
                ax.set_ylim([1.1e-1, 2e2])
                setLegend(ax, fontsize=10)
    fi.text(0.5, 0.00, 'Phonon Frequency (THz)', ha='center')
    fi.text(
        0.03, 0.5, 'Relaxation Time (ps)', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
