# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-10-23 17:53:02
import os
os.chdir("bin")
os.system("cp ../*.tex .")
os.system('latexdiff paper.tex paper-last.tex>diff.tex')
os.system('latex diff.tex')
os.system('bibtex diff')
os.system('latex diff.tex')
os.system('latex diff.tex')
os.system("dvipdft diff")
