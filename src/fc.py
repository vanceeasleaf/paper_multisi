# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 14:39:58
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-28 00:02:58
import aces.tools as tl
from aces.graph import fig, pl
import numpy as np
from aces.f import capacity
from aces.algorithm.kpoints import filter_along_direction as fad
from ase import io
from aces.io.phonopy.fc import readfc2, readfc3
text_style = dict(
    horizontalalignment='left',
    verticalalignment='center',
    fontsize=12,
    fontdict={'family': 'serif'})
vs = '2l1,2l2,2l3,2lh,2lr,3l1,3l2,4l1,5l1,6l1,8l1,Silicene'.split(',')
with fig('cv.eps'):
    fi, axes = pl.subplots(figsize=(10, 7))
    for i, v in enumerate(vs):
        print(v)
        ax = axes
        if v == "2lh":
            v = "2lhex"
        if v == "2lr":
            v = "2lrt3"
        file = v + "/0/secondorder/FORCE_CONSTANTS"
        fc2 = readfc2(file)
        atoms = io.read(v + "/0/secondorder/POSCAR")

        # ax.text(.02,.8,"("+v+")",transform=ax.transAxes,**text_style)
    ax.bar(ind, np.array(cv1) / 1000, width, color='r')
    ax.bar(ind + width, np.array(cv2) / 1000, width, color='y')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(vs)
    #fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(
        0.04,
        0.5,
        'Phonon Heat Capacity ($kJ/m^3/K$)',
        va='center',
        rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
