from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="multi_silicene",
			method="greenkubo",
			nodes=6,
			procs=6,
			queue="q1.1",
			runTime=10000000
			,runner="shengbte"
		)
		app=dict(supercell=[3,3,1],kpoints=[15,15,1],poscar='8l1')
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
