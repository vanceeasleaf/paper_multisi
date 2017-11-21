# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-14 22:16:16
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-11-20 22:08:46
from aces.tools import *
from aces.graph import fig, setLegend, pl, fit
import numpy as np

from ase import io

kas = []
with fig('chi.eps', figsize=(7, 8)):
    markers = ['s', '8', '^', 'D', '>']
    colors = "k,r,b,purple,g,o".split(',')
    text_style = dict(horizontalalignment='left', verticalalignment='center',
                      fontsize=14, fontdict={'family': 'serif'})
    fi, axes = pl.subplots(1, 1, sharex=True, figsize=(7, 4))
    ax1 = axes
    ks = []
    vs = '2l1,2l2,2lhex,3l1,4l1,5l1,6l1,8l1'.split(',')
    for i, v in enumerate(vs):

        dir = "%s/0/SHENG" % v
        if v == "2l1":
            dir = "2l1/0/sheng.1"
        kappa = np.loadtxt(
            dir + '/T300K/BTE.cumulative_kappa_tensor')  # [::3]
        # m = markers[i]
        # c = colors[i]
        l = kappa[:, 0]
        atoms = io.read(v + "/0/secondorder/POSCAR")
        nlayer = int(v.split('l')[0])
        ss = np.linalg.norm(atoms.cell[2]) / (
            3.34 * nlayer)

        z = kappa[:, 1] * ss
        a = kappa[:, 5] * ss
        opts = dict(
            # markeredgecolor='w',
            # marker=m,
            # color=c,
            # markersize=1 + 2,
            lw=2,
            ls='-')
        o1 = "-"
        ka = np.abs(z - a) / np.max(np.c_[z, a], axis=1)
        label = v
        ax1.semilogx(l, ka, label=label, **opts)
        ax1.set_xlabel("Cutoff Mean Free Path for Phonons (Angstrom)")
        # ax1.set_ylim([0, 15])
        ax1.set_xlim([10, 1e5])
        ax1.set_ylim([0, .8])
        ax1.set_ylabel("Thermal Conductivity Anisotropy")
        # ax1.text(-.15, 1, 'b)', transform=ax1.transAxes, **text_style)
    setLegend(ax1, ncol=2, loc=0, fontsize=8)
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
