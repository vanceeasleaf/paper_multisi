# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 16:26:09
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-17 14:15:28
from aces.tools import *
from ase import io
from aces.graph import fig,setLegend,pl,fit
import numpy as np
text_style = dict(horizontalalignment='left', verticalalignment='center',
              fontsize=12, fontdict={'family': 'serif'})
vs='2l1  2l2  2l3  2lh  2lr3  3l1  3l2  4l1  5l1  6l1  8l1  Silicene'.split()
import matplotlib
matplotlib.rcParams['axes.linewidth'] = 0
with fig('prq.png'):

	fi,axes=pl.subplots(3,4,figsize=(10,7), subplot_kw=dict(projection='polar'))
	print vs
	for i,v in enumerate(vs):
		ax=axes[i//4,i%4]
		if v=="2lh":
			v="2lhex"
		if v=="2lr3":
			v="2lrt3"
		#shell_exec("cd %s/0/secondorder/; ae drawpr"%v)
		file=v+"/0/secondorder/prq.txt"
		y=np.loadtxt(file)
		"""
		poscar=v+"/0/POSCAR"
		atoms=io.read(poscar)
		rcell=atoms.get_reciprocal_cell()
		yy=[]
		for x in y:
			xx=x[:3].dot(rcell)
			yy.append(xx)
		yy=np.array(yy)
		"""
		N=30
		dth=2*np.pi/N
		ths=np.arange(0,N)*dth
		prs=[]
		thi=np.arctan2(y[:,1],y[:,0])#*180/np.pi
		thi[thi < 0] += 2*np.pi
		for th in ths:
			fil=(thi>th-.5*dth)*(thi<=th+.5*dth)
			if fil.sum()>0:
				xx=y[fil,4].mean()
			else:
				xx=None
			prs.append(xx)
		ax.plot(ths,prs,lw=2,color='r')
		# for periodic
		ax.plot(np.array(ths)[[-1,0]],np.array(prs)[[-1,0]],lw=2,color='r')
		ax.set_rlim([0,1.2])
		ax.set_rticks([])

		ax.text(.02,.8,"("+v+")",transform=ax.transAxes,**text_style)
		if i>0:
			ax.set_xticks([])
	fi.subplots_adjust(left = None, bottom = None, right  = None, top = None, wspace = 0, hspace = 0 )