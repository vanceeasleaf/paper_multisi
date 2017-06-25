# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-25 22:59:03
import os
if not os.path.exists("bin/"):
    os.mkdir("bin")
os.chdir("bin")
if not os.path.exists("images/"):
    os.mkdir("images")
os.system("cp ../fudan_logo_vector.eps .")
os.system("cp ../../latex/ref.bib .")
os.system("cp ../../src/*.eps images/")
os.system('xelatex ../presentation.tex')
os.system('xelatex ../presentation.tex')
#os.system('bibtex presentation')
#os.system('latex ../presentation.tex')
#os.system('latex ../presentation.tex')
#os.system("dvipdft presentation")
