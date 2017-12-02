# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-12-02 11:28:15
import os
if not os.path.exists("bin/"):
    os.mkdir("bin")
os.chdir("bin")
if not os.path.exists("images/"):
    os.mkdir("images")
os.system("cp ../fudan_logo_vector.eps .")
os.system("cp ../ref.bib .")
os.system("cp ../../src/*.eps images/")
os.system("cp ../*.tex .")
os.system('xelatex presentation.tex')
os.system('bibtex presentation')
os.system('xelatex ../presentation.tex')
os.system("rm *.tex *.aux *.bbl *.blg *.dvi *.log *.bib *.out")
