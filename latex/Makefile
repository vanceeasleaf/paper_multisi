TEX = latex

paper : paper.tex
	which python
	python run.py
pre : presentation.tex 
	python run_pre.py 
diff : paper.tex paper-last.tex
	python run_diff.py
		 
.PHONY:clean

clean : 
	rm -r bin
