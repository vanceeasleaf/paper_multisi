# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-19 17:05:44

import aces.tools as tl
from aces.graph import fig, setLegend, pl
import numpy as np
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')
import matplotlib
matplotlib.rcParams['ytick.minor.width'] = 1.5
matplotlib.rcParams['ytick.minor.size'] = 3
with fig('tao2l.png'):
    fi, axes = pl.subplots(1, 3, sharex=True, sharey=True, figsize=(10, 7))
    for j in range(3):
        if j == 0:
            vs = "2l1,2l2,2lhex".split(',')
        if j == 1:
            vs = "3l1,3l2,4l1".split(',')
        if j == 2:
            vs = "5l1,6l1,Silicene".split(',')
        for i, v in enumerate(vs):
            ax = axes[j]
            file = "%s/0/SHENG/T300K/q_tao.txt" % v
            if v == "2l1":
                file = "2l1/0/sheng.1/T300K/q_tao.txt"
            if not tl.exists(file):
                tl.shell_exec("cd %s/0/SHENG/;ae post" % v)
            y = np.genfromtxt(file, delimiter='\t', skip_header=1)
            c = ['w', 'k'][colors[i] == 'k']
            th = np.arctan2(y[:, 1], y[:, 0])
            dth = 2.0 * np.pi / 30
            fil = (th < dth) * (th > -dth)
            ax.semilogy(
                y[fil, 3],
                y[fil, 4],
                ls='.',
                marker=markers[i],
                markersize=6,
                markeredgecolor=colors[i],
                color=c,
                label=v)
            ax.set_xlim([0, 4.9])
            ax.set_ylim([0, 1e4])
            setLegend(ax, fontsize=10)
    fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(
        0.05, 0.5, 'Relaxation Time (ps)', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
