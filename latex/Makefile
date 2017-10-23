TEX = latex
diff : paper.tex paper-last.tex
	python run_diff.py

paper : paper.tex
	which python
	python run.py
pre : presentation.tex 
	python run_pre.py 
		 
.PHONY:clean

clean : 
	rm -r bin
