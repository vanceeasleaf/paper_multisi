# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 14:39:58
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-11-22 11:43:17
import aces.tools as tl
from aces.graph import fig, setLegend, pl
import numpy as np
from aces.f import binmeanx
from aces.io.shengbte import get_w_final, get_qpoints, get_omega, get_tau, get_v
text_style = dict(
    horizontalalignment='left',
    verticalalignment='center',
    fontsize=12,
    fontdict={'family': 'serif'})
vs = '2l1,2lh,3l1,4l1,5l1,6l1'.split(',')
with fig('gv.eps'):
    fi, axes = pl.subplots(2, 3, sharex=True, sharey=True, figsize=(10, 7))
    for i, v in enumerate(vs):
        print(v)
        ax = axes[i // 3, i % 3]
        if v == "2lh":
            v = "2lhex"
        if v == "2lr":
            v = "2lrt3"
        dir = "%s/0/SHENG" % v
        # file = v + "/0/secondorder/groupv/mesh.yaml"
        # data = tl.parseyaml(file)
        # freqs = []
        # gvs = []
        # for phonon in data['phonon']:
        #     qp = phonon['q-position']
        #     for band in phonon['band']:
        #         frequency = band['frequency']
        #         gv = np.array(band['group_velocity'])
        #         freqs.append(frequency)
        #         gvs.append(gv)
        omega = get_omega(dir)
        cv = get_v(dir)
        freqs = omega.flatten()
        gvs = np.c_[cv[:, :, 0].flatten(), cv[:, :, 1].flatten()]
        freqs = np.array(freqs)
        gvs = np.array(gvs)
        gvs = np.abs(gvs)
        N = 40
        df = 20.0 / N
        v1 = v
        if v1 == '2lhex':
            v1 = '2l3'
        x, y = binmeanx(np.c_[freqs, gvs[:, 0]], [0, 20], df)
        ax.plot(x, y, color="k", lw=3, label=v1 + "z")
        x, y = binmeanx(np.c_[freqs, gvs[:, 1]], [0, 20], df)
        ax.plot(x, y, color="r", ls="--", lw=3, label=v1 + "a")
        # ax.text(.02,.8,"("+v+")",transform=ax.transAxes,**text_style)
        setLegend(ax, ncol=1, fontsize=10)
        # ax.set_yticks([])
        ax.set_xlim([0.05, 19.9])
        ax.set_ylim([0.05, None])

    fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(
        0.07,
        0.5,
        'Phonon Group Velocity (A/ps)',
        va='center',
        rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
