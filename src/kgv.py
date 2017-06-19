# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 14:39:58
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-19 18:53:51
from aces.tools import *
from aces.graph import fig, setLegend, pl, fit
import numpy as np
text_style = dict(
    horizontalalignment='left',
    verticalalignment='center',
    fontsize=12,
    fontdict={'family': 'serif'})
vs = '2l1,2l2,2l3,2lh,2lr,3l1,3l2,4l1,5l1,6l1,8l1,Silicene'.split(',')
with fig('kgv.png'):
    fi, axes = pl.subplots(1, 1, sharex=True, sharey=True, figsize=(10, 7))
    for i, v in enumerate(vs):
        print v
        ax = axes  # [i // 6, i % 6]
        if v == "2lh":
            v = "2lhex"
        if v == "2lr":
            v = "2lrt3"
        file = v + "/0/secondorder/groupv/mesh.yaml"
        data = parseyaml(file)
        freqs = []
        gvs = []
        qps = []
        for phonon in data['phonon']:
            qp = phonon['q-position']
            gvs0 = []
            for band in phonon['band']:
                frequency = band['frequency']
                gv = np.array(band['group_velocity'])
                freqs.append(frequency)
                gvs0.append(gv)
            qps.append(qp)
            gvs.append(gvs0[0])
        freqs = np.array(freqs)
        gvs = np.array(gvs)
        qps = np.array(qps)
        pl.quiver(qps[:, 0], qps[:, 1], gvs[:, 0], gvs[:, 1], alpha=.5)
        break
        gvs = np.abs(gvs)
        ff = []
        gg = []
        N = 40
        df = 20.0 / N
        for i in range(N):
            fil = (freqs > i * df) * (freqs < (i + 1) * df)
            ff.append(i * df)
            if fil.sum() == 0:
                gg.append(0)
            else:
                gg.append(gvs[fil].mean(axis=0))
        gg = np.array(gg)
        ax.plot(ff, gg[:, 0], color="k", lw=3, label=v + "z")
        ax.plot(ff, gg[:, 1], color="r", ls="--", lw=3, label=v + "a")
        # ax.text(.02,.8,"("+v+")",transform=ax.transAxes,**text_style)
        setLegend(ax, ncol=1, fontsize=10)
        ax.set_yticks([])
        ax.set_xlim([0, 5.9])

    fi.text(0.5, 0.04, 'Frequency (THz)', ha='center')
    fi.text(
        0.07,
        0.5,
        'Phonon Group Velocity (A/ps)',
        va='center',
        rotation='vertical')
    fi.subplots_adjust(
        left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
