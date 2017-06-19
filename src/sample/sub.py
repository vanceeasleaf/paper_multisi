from aces import Aces
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="multi_silicene",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="phonopy"
		)
		app=dict(supercell=[3,3,1],kpoints=[5,5,1],file='2l1')
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
