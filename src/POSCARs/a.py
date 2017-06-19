from aces.tools import *
from aces.io.vasp import writevasp
files=ls("*.vasp")
from ase import io,Atoms
for file in files:
	f=open(file)
	line=f.next()
	lc=float(line)
	cell=[]
	for i in range(3):
		a=map(float,f.next().split())
		print(a)
		cell.append(a)
	natom=int(f.next())
	s=[]
	for i in range(natom):
		 a=map(float,f.next().split())
		 s.append(a)
	atoms=Atoms('Si'+str(natom),scaled_positions=s,cell=cell)
	writevasp(atoms,file.replace('vasp','POSCAR'))
