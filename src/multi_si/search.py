# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-14 22:16:16
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-14 22:25:45
from aces.tools import *
files=shell_exec("find . -name Thermal_conductivity.txt").split('\n')
for file in files:
	print file.split('/')[1],file
	cp(file,"tc/"+file.split('/')[1]+".txt")