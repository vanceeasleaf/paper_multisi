# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-15 16:27:39
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-16 14:10:26
from aces.tools import *
from aces.graph import fig,setLegend,pl,fit
import numpy as np

vs=np.array('2l1,2l2,3l1,4l1,6l1,10l1'.split(',')).reshape([2,3])
ch='abcdef'
text_style = dict(horizontalalignment='left', verticalalignment='center',
              fontsize=14, fontdict={'family': 'serif'})
import matplotlib
matplotlib.rcParams['xtick.major.width'] = 0
with fig('bands.png'):
	fi,axes=pl.subplots(2,3,sharex=True,sharey=True,figsize=(10,7))
	for i in range(2):
		for j in range(3):
			label=ch[i*3+j]+")"
			v=vs[i,j]
			file="multisi_phonon/"+v
			y=np.loadtxt(file,skiprows=2)
			k=y[:,3]
			fq=y[:,4:]
			m=fq.shape[1]
			#for mi in range(m):	
			G1=0.707107
			X=1.20711
			Y=1.91421
			G2=2.41421
			LX=X-G1
			LY=G2-Y
			L=LX+LY
			fil=(k>G1-0.02)*(k<X+0.02) # G->X
			axes[i,j].plot(X-k[fil][::-1],fq[fil][::-1],color='k',alpha=0.9)
			fil=(k>Y-0.02)*(k<G2+0.02) # Y->G
			axes[i,j].plot(G2-k[fil][::-1]+LX,fq[fil][::-1],color='k',alpha=0.9)
			axes[i,j].text(.05,.95,label,transform=axes[i,j].transAxes,**text_style)
			axes[i,j].set_xticks([])
			#axes[i,j].set_xlim([0,2.41421])
			#axes[i,j].set_xlim([0,L])
			axes[i,j].set_ylim([0,19])
			#t=(0+0.1,0.707107,1.20711,1.91421,2.41421-0.1);
			#labels=("K",r"$\Gamma$","X","Y",r"$\Gamma$")
			t=(0+0.1,LX,L-0.1);
			labels=("X",r"$\Gamma$","Y")
			if j==0:
				axes[i,j].set_ylabel("Frequency (THz)")
			if i==0:
				labels=['']*len(labels)
			pl.xticks(t,labels)
			for ti,tt in enumerate(t):
				if ti==0 or ti==len(t)-1:continue
				axes[i,j].axvline(x=tt,linestyle='--',  linewidth=.5, color='black')
	fi.subplots_adjust(left = None, bottom = None, right  = None, top = None, wspace = 0, hspace = 0 )
