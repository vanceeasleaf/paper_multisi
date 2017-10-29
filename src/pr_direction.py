# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 16:26:09
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-10-28 16:07:45

from aces.graph import fig, setLegend, pl
from aces.algorithm.kpoints import filter_along_direction as fad
import numpy as np
from aces.f import binmeanx
text_style = dict(horizontalalignment='left', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'serif'})
vs = '2l1  2lh  3l1   4l1  5l1  6l1'.split()
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')
with fig('pr_direction.eps'):

    fi, axes = pl.subplots(
        2, 3, sharex=True, sharey=True, figsize=(10, 6))
    print(vs)
    for j in range(2):
        vv = np.array(vs).reshape([2, 3])[j]
        for i, v in enumerate(vv):
            for s in ['z', 'a']:
                ax = axes[j, i]
                if v == "2lh":
                    v = "2lhex"
                if v == "2lr3":
                    v = "2lrt3"
                #shell_exec("cd %s/0/secondorder/; ae drawpr"%v)
                file = v + "/0/secondorder/prq.txt"
                y = np.loadtxt(file)
                dth = np.pi / 10
                if s == "z":
                    phi = 0.0
                else:
                    phi = np.pi / 2.0
                fil = fad(y, phi, dth)
                q = y[fil][:, [3, 4]]
                x, y = binmeanx(q, [0, 20.9], 1.5)
                mfc = [colors[0], 'w'][s == 'a']
                ls = ['-', '-.'][s == 'a']
                ax.plot(x, y, ls=ls,
                        marker=markers[0],
                        markersize=9,
                        markeredgecolor=colors[0],
                        markerfacecolor=mfc,
                        color=colors[0], label=v + s)
                ax.set_xlim([0, 20.9])
                ax.set_ylim([0, 1.2])
                setLegend(ax, fontsize=10)
    fi.text(0.5, 0.04, 'Phonon Frequency(THz)', ha='center')
    fi.text(
        0.05,
        0.5,
        'Phonon Participation Ratio',
        va='center',
        rotation='vertical')
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
