# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-23 19:26:23


from aces.graph import fig, setLegend, pl
import numpy as np
from aces.algorithm.kpoints import filter_along_direction as fad
from aces.io.shengbte import get_qpoints_full as gqf, get_tau, get_omega
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')
import matplotlib
matplotlib.rcParams['ytick.minor.width'] = 1.5
matplotlib.rcParams['ytick.minor.size'] = 3
with fig('tau.eps'):
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

                xx = []
                dp = 0.4
                for p in np.arange(0.0, 5.0, dp):
                    f1 = (q[:, 0] <= (p + dp)) * (q[:, 0] > p)
                    if f1.any():
                        xx.append([p + dp * .5, q[f1, 1].mean()])
                xx = np.array(xx)
                mfc = [colors[i], 'w'][s == 'a']
                ls = ['-', '-.'][s == 'a']
                if len(xx) == 0:
                    break
                ax.semilogy(
                    xx[:, 0],
                    xx[:, 1],
                    ls=ls,
                    marker=markers[i],
                    markersize=9,
                    markeredgecolor=colors[i],
                    markerfacecolor=mfc,
                    color=colors[i],
                    label=v + s)
                ax.set_xlim([0, 4.55])
                ax.set_ylim([1e-0, 1e3])
                setLegend(ax, fontsize=10)
    fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(
        0.05, 0.5, 'Relaxation Time (ps)', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
