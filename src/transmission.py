# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   1970-01-01 08:00:00
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-21 22:19:29
from aces.tools import *
from ase import io
from aces.graph import fig, setLegend, pl, fit
import matplotlib
matplotlib.rcParams['xtick.major.width'] = 1
matplotlib.rcParams['ytick.major.width'] = 1
import numpy as np
text_style = dict(horizontalalignment='left', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'serif'})
vs = '2l1  2l2  2l3  2lh  2lr3  3l1  3l2  4l1  5l1  6l1  8l1  Silicene'.split()
with fig('transmission.eps'):
    fi, axes = pl.subplots(6, 2, sharex=True, sharey=False, figsize=(10, 7))
    for i, v in enumerate(vs):
        ax = axes[i // 2, i % 2]
        file = "negf/" + v + "/transmission.txt"
        f = np.loadtxt(file, skiprows=1)
        freq = f[:, 0]
        trans = f[:, 3]
        atoms = io.read("negf/" + v + "/center/SPOSCAR")
        cross = np.linalg.norm(
            atoms.cell[1]) * (atoms.positions[:, 2].max() - atoms.positions[:, 2].min())

        ax.plot(freq, trans / cross, color="k", label=v + "z")
        # ax.fill_between(freq, 0, trans / cross, color='r', alpha=0.5)
        ax.text(.02, .8, "(" + v + ")", transform=ax.transAxes, **text_style)
        file = "negfa/" + v + "/transmission.txt"
        f = np.loadtxt(file, skiprows=1)
        freq = f[:, 0]
        trans = f[:, 3]
        atoms = io.read("negfa/" + v + "/center/SPOSCAR")
        cross = np.linalg.norm(
            atoms.cell[0]) * (atoms.positions[:, 2].max() - atoms.positions[:, 2].min())

        # ax.plot(freq, trans / cross, color="k", ls="--", label=v + "")
        ax.fill_between(freq, 0, trans / cross, color='r', alpha=0.5)
        ax.set_yticks([])
        ax.set_yticklabels([])
        # ax.set_ylabel("Phonon Transmission")
        # ax.set_xlabel("Frequency (THz)")
        ax.set_xlim([0, 22])
        # setLegend(ax, fontsize=9)
    #ax.set_xlabel("Frequency (THz)")
    fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(0.07, 0.5, 'Phonon Transmission', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
