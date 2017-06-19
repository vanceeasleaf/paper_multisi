# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-16 18:34:55
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-16 19:38:54



from aces.tools import *
from ase import io
from aces.graph import fig,setLegend,pl,fit
import numpy as np
markers=['^','s',"8"]
colors="k,r,b,g,purple".split(',')
import matplotlib
matplotlib.rcParams['ytick.minor.width'] = 1.5
matplotlib.rcParams['ytick.minor.size'] = 3
with fig('gru.png'):
	fi,axes=pl.subplots(1,3,sharex=True,sharey=True,figsize=(10,7))
	for j in range(3):
		if j==0:
			vs="2l1,2l2,2lhex".split(',')
		if j==1:
			vs="3l1,3l2,4l1".split(',')
		if j==2:
			vs="5l1,6l1,Silicene".split(',')
		for i,v in enumerate(vs):
			ax=axes[j]
			file="%s/0/SHENG/T300K/gruneisen_freq.txt"%v
			if v=="2l1":
				file="2l1/0/sheng.1/T300K/gruneisen_freq.txt"
			if not exists(file):
				shell_exec("cd %s/0/SHENG/;ae postnew"%v)
			y=np.genfromtxt(file,delimiter='\t',skip_header=1)
			hist,bin_edges=np.histogram(y[:,1],bins=60,range=[-2,5],density=True)
			ax.plot(bin_edges[1:],hist,color=colors[i],label=v,lw=2)
			ax.set_xlim([-2,4.9])
			setLegend(ax,fontsize=10)
	fi.text(0.5, 0.04, 'Gruneisen Parameter', ha='center')
	fi.text(0.05, 0.5, 'Probability', va='center', rotation='vertical')
	fi.subplots_adjust(left = None, bottom = None, right  = None, top = None, wspace = 0, hspace = 0 )
