# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-10-23 22:03:37
import os
import re
os.chdir("bin")
os.system("cp ../*.tex .")
os.system('latexdiff paper-last.tex paper.tex >diff.tex')
f = open('diff.tex', encoding="utf-8")
s = f.read()
s = re.sub(r'({[^}]*)\n\n([^}]*})', r'\1\2', s)
f.close()
f = open('diff.tex', 'w', encoding="utf-8")
f.write(s)
f.close()
os.system('latex diff.tex')
os.system('bibtex diff')
os.system('latex diff.tex')
os.system('latex diff.tex')
os.system("dvipdft diff")
