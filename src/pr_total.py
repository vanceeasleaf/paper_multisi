# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   1970-01-01 08:00:00
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-21 16:30:08
from aces.tools import *
from aces.graph import fig, setLegend, pl, fit
import numpy as np

vs = '2l1,2l2,2l3,2lh,2lr,3l1,3l2,4l1,5l1,6l1,8l1,Silicene'.split(',')
p = []
error = []
with fig('pr_total.eps'):
    for v in vs:
        if v == "2lh":
            v = "2lhex"
        if v == "2lr":
            v = "2lrt3"
        file = v + "/0/secondorder/pr.txt"
        y = np.loadtxt(file)
        print y
        u = y[:, 1].mean()
        p.append(u)
        e = y[:, 1].std()
        error.append(e)
    fig, ax = pl.subplots()
    pos = []
    b = 0.0
    for i in range(5):
        b = b + 0.5
        pos.append(b)
    b += 0.5
    for i in range(2):
        b = b + 0.5
        pos.append(b)
    for i in range(5):
        b = b + 1
        pos.append(b)
    ax.bar(
        pos,
        p,
        yerr=error,
        align='center',
        color='g',
        ecolor='black',
        width=0.3,
        error_kw=dict(
            elinewidth=2,
            ecolor='black'))
    ax.set_xticks(pos)
    ax.set_xticklabels(vs)
    ax.set_xlabel('Structure')
    ax.set_ylabel("Average Phonon Participation Ratio")
