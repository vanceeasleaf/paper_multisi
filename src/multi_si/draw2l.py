# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-14 22:16:16
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-15 15:06:29
from aces.tools import *
from aces.graph import fig,setLegend,pl,fit
import numpy as np 
files=ls("tc/*.txt")
markers=['s','8','^','D','>']
colors="k,r,g,b,purple".split(',')
vs='2l1,2l2,2l3,2lr3,2lh'.split(',')
def ff(p,x):
	return p[0]*(1.0-np.exp(-x/p[1]))
	#return 1.0/(p[1]/x+1/p[0])-p[2]
	#return p[0]*p[1]**x


with fig('2l.png'):
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
			pl.plot(y[:,0],y[:,1],label=label,**opts)
			p=fit(y[:,0],y[:,1],[1,1,1],ff)
			xx=np.linspace(10,100,1000)
			pl.plot(xx,ff(p,xx),color=c,ls=o1)
			pl.xlabel("Length(nm)")
			pl.ylim([0,14])
			pl.ylabel("Thermal Conductivity(W/mK)")
	setLegend(pl,ncol=2,fontsize=10)
