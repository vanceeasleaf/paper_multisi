# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 14:39:58
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-26 22:48:19
import aces.tools as tl
from aces.graph import fig, pl
import numpy as np
from aces.f import capacity
from aces.algorithm.kpoints import filter_along_direction as fad
from ase import io
text_style = dict(
    horizontalalignment='left',
    verticalalignment='center',
    fontsize=12,
    fontdict={'family': 'serif'})
vs = '2l1,2l2,2l3,2lh,2lr,3l1,3l2,4l1,5l1,6l1,8l1,Silicene'.split(',')
with fig('cv.eps'):
    fi, axes = pl.subplots(figsize=(10, 7))
    N = len(vs)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    cv1 = []
    cv2 = []
    for i, v in enumerate(vs):
        print(v)
        ax = axes
        if v == "2lh":
            v = "2lhex"
        if v == "2lr":
            v = "2lrt3"
        file = v + "/0/secondorder/groupv/mesh.yaml"
        data = tl.parseyaml(file)
        freqs = []
        qpoints = []
        for phonon in data['phonon']:
            qp = phonon['q-position']
            for band in phonon['band']:
                frequency = band['frequency']
                gv = np.array(band['group_velocity'])
                freqs.append(frequency)
                qpoints.append(qp)
        freqs = np.array(freqs)
        qpoints = np.array(qpoints)
        dth = np.pi / 10
        phi = 0.0
        fil = fad(qpoints, phi, dth)
        atoms = io.read(v + "/0/secondorder/POSCAR")
        V = np.linalg.norm(atoms.cell[0]) * np.linalg.norm(atoms.cell[1]) * (
            atoms.positions[:, 2].max() - atoms.positions[:, 2].min())
        cv = capacity(freqs[fil], 300, V).mean()
        print("cv1", cv)
        cv1.append(cv)

        phi = np.pi / 2.0
        fil = fad(qpoints, phi, dth)
        cv = capacity(freqs[fil], 300, V).mean()
        print("cv2", cv)
        cv2.append(cv)
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
