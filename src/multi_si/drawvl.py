# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-14 22:16:16
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-15 15:05:11
from aces.tools import *
from aces.graph import fig,setLegend,pl,fit
import numpy as np

def ff(p,x):
	return p[0]*(1.0-np.exp(-x/p[1]))
	#return 1.0/(p[1]/x+1/p[0])-p[2]
	#return p[0]*p[1]**x


with fig('vla.png',figsize=(7,8)):
	markers=['s','8','^','D','>']
	colors="k,r,b,purple,g".split(',')
	vs='3l1,3l2,4l1,5l1'.split(',')
	text_style = dict(horizontalalignment='left', verticalalignment='center',
                  fontsize=14, fontdict={'family': 'serif'})
	fi,axes=pl.subplots(2,1,sharex=True,figsize=(7,8))
	ax1=axes[0]
	for s in ['z','a']:
		for i,v in enumerate(vs):
		
			file="tc/%s.txt"%(v+s)
			m=markers[i]
			c=colors[i]
			if s=='z':
				opts=dict(markeredgecolor='w',marker=m,color=c,markersize=8+2,ls='.')
				o1="-"
			else:
				opts=dict(markeredgecolor=c,marker=m,color='w',markersize=8,ls='.')
				o1="--"
			y=np.loadtxt(file,skiprows=2)[:,[1,5]]
			print y
			label=file.replace("tc/","").replace(".txt","")
			ax1.plot(y[:,0],y[:,1],label=label,**opts)
			p=fit(y[:,0],y[:,1],[1,1,1],ff)
			xx=np.linspace(10,100,1000)
			ax1.plot(xx,ff(p,xx),color=c,ls=o1)
			ax1.set_ylabel("Thermal Conductivity(W/mK)")
			#ax1.set_xticks([])
			ax1.set_ylim([0,14])
			ax1.text(-.15,1,'a)',transform=ax1.transAxes,**text_style)
	setLegend(ax1,ncol=2,loc=0,fontsize=8)
	ax1=axes[1]
	vs='8l1,10l1,si111,6l1'.split(',')
	for s in ['z','a']:
		for i,v in enumerate(vs):
		
			file="tc/%s.txt"%(v+s)
			m=markers[i]
			c=colors[i]
			if s=='z':
				opts=dict(markeredgecolor='w',marker=m,color=c,markersize=8+2,ls='.')
				o1="-"
			else:
				opts=dict(markeredgecolor=c,marker=m,color='w',markersize=8,ls='.')
				o1="--"
			y=np.loadtxt(file,skiprows=2)[:,[1,5]]
			print y
			label=file.replace("tc/","").replace(".txt","")
			ax1.plot(y[:,0],y[:,1],label=label,**opts)
			p=fit(y[:,0],y[:,1],[1,1,1],ff)
			xx=np.linspace(10,100,1000)
			ax1.plot(xx,ff(p,xx),color=c,ls=o1)
			ax1.set_xlabel("Length(nm)")
			ax1.set_ylim([0,37])
			ax1.set_ylabel("Thermal Conductivity(W/mK)")
			ax1.text(-.15,1,'b)',transform=ax1.transAxes,**text_style)
	setLegend(ax1,ncol=2,loc=0,fontsize=8)

	fi.subplots_adjust(left = None, bottom = None, right  = None, top = None, wspace = 0, hspace = 0 )