# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-27 14:58:52
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-27 22:50:00

import aces.tools as tl
from aces.graph import fig, pl
from aces.algorithm.kpoints import filter_along_direction as fad
import numpy as np
from ase import io
from aces.io.phonopy.meshyaml import get_eigs, get_pr, meshyaml
text_style = dict(horizontalalignment='left', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'serif'})
vs = '2l1  2l2  2l3  2lh  2lr3  3l1  3l2  4l1  5l1  6l1  8l1  Silicene'.split()
markers = ['^', 's', "8"]
colors = "k,r,b,g,purple".split(',')


def write_dump(poscar, color, file):
    atoms = io.read(poscar)
    cell = atoms.get_cell()
    natom = len(atoms)
    s = """ITEM: TIMESTEP
0
ITEM: NUMBER OF ATOMS
%d
ITEM: BOX BOUNDS pp pp pp
0 %.6f
0 %.6f
0 %.6f
""" % (natom, cell[0, 0], cell[1, 1], cell[2, 2])
    s += "ITEM: ATOMS id xs ys zs color\n"
    ss = atoms.get_scaled_positions()
    for i in range(natom):
        s += str(i + 1) + ' ' + tl.toString(ss[i]) + " " + str(color[i]) + "\n"
    tl.write(s, file)

for j in range(3):
    vv = np.array(vs).reshape([3, 4])[j]
    for i, v in enumerate(vv):
        for s in ['z', 'a']:
            if v == "2lh":
                v = "2lhex"
            if v == "2lr3":
                v = "2lrt3"
            file = v + "/0/secondorder/mesh.npz"
            poscar = v + "/0/secondorder/POSCAR"

            qpoints, freqs, eigs = get_eigs(file)
            dth = np.pi / 10
            if s == "z":
                phi = 0.0
            else:
                phi = np.pi / 2.0
            fil = fad(qpoints, phi, dth)

            # shape=(natom). the average amplitude of each atom
            c = np.linalg.norm(eigs, axis=-1)[fil]

            c = c.mean(axis=0).mean(axis=0)
            tl.mkdir("color/")
            write_dump(poscar, c, "color/" + v + s + ".lammpstrj")
