TEX = latex

paper : paper.tex
	which python
	python run.py
pre : presentation.tex 
	python run_pre.py 
		 
.PHONY:clean

clean : 
	rm -r bin
