from Ipt_module import *
from Params import *
Params()

import lammps_tools as lmp


class CreateLAMMPSFile():

	_same_mol_flag_ideal = 0	
	_paramsFolder = '%s/data_files/'%glb_path
	_lmpsTemplate = _paramsFolder+'lammps_template.in'

	def __init__(self,celltype,chrId,runId,nNode,ncpu,ptn,time,lmpsdir,nearCtcfThreshold,runStep):

		self.celltype           = celltype
		self.chrId              = chrId
		self.runId              = runId
		self.nNode              = nNode
		self.ncpu               = ncpu
		self.ptn                = ptn
		self.time               = time
		self.lmpsdir            = lmpsdir
		self.nearCtcfThreshold  = nearCtcfThreshold
		self.runStep            = runStep


	def assignType(self,seqfile,hp):
	# ----  assign the states based on seqfile 
		hp.atom_types = []
		seq = []
		for ics in range(1,ncs+1):
			hp.add_atom_type(1.0, None, None)
		for line in fi.input(seqfile):
			seq.append(int(line.split()[1]))
		for ia, atom in enumerate(hp.atoms):
			atom['atom_type_i'] = seq[ia]


	def createLAMMPSDataFile(self):
		_ctcfFile 	='''%s/../ctcfBindingSites/processedCTCF/model_input/%s/ctcf_position_%s_chr%d_From%dMbTo%dMb.txt'''\
				%(glb_path,self.celltype,self.celltype,self.chrId,chr_region[self.chrId-1,1],chr_region[self.chrId-1,2])
		_lmpsFolder	='%s/run_folder/%s/lmps_data'%(glb_path,self.celltype)

		# ----  specify bond and angle
		hp = lmp.Data()
		hp.add_bond_type(bond_coeffs,comment)
		hp.add_angle_type(angle_coeffs,comment)
		hp.read_from_file('%s/data_files/data.chromosome.init'%glb_path)
	 
		# ----  assign atom types
		self.assignType(_ctcfFile,hp)
		
		if not os.path.exists(_lmpsFolder):
			os.makedirs(_lmpsFolder)
		hp.write_to_file('%s/data.chromosome'%_lmpsFolder,ellipsoidFlag=0)		


	def createLAMMPSInputFile(self):
		global _rundir
		_rundir = "%s/run_folder/%s/chr%d/run%02d/"%(glb_path,self.celltype,self.chrId,self.runId)
		_csFile='%s/../chromatinStates/model_input/%s/%s_chr%d_chromatin_states.txt'\
				%(glb_path,self.celltype,self.celltype,self.chrId)
		_ctcfIndFile = '''%s/../ctcfBindingSites/processedCTCF/model_input/%s/ctcf_index_%s_chr%d_From%dMbTo%dMb.txt'''\
				%(glb_path,self.celltype,self.celltype,self.chrId,chr_region[self.chrId-1,1],chr_region[self.chrId-1,2])

		if not os.path.exists(_rundir):
			os.makedirs(_rundir)

		# lammps input file with custom random seed
		_inFile = _rundir + "in.chromosome"
		in_tmp = fi.input(self._lmpsTemplate)
		pf = open(_inFile, 'w')
		pf.write('variable        rseed equal   %d\n'%(4928459+self.runId) )
		for line in in_tmp:
			if line[0:10] == 'pair_style':
				pf.write(
'''pair_style        hybrid/overlay table linear 10000 tanhlr/cut/ideala 6.0 %d 15 %s/ucs_chrom.txt %s tanhlr/cut/ideal 6.0 %s/uctcf_chrom.txt %s 0.75 %d\n'''\
%(self._same_mol_flag_ideal,\
self._paramsFolder,_csFile,\
self._paramsFolder,_ctcfIndFile,self.nearCtcfThreshold))
			elif line[0:3] == 'run':
				pf.write('run        %d'%(self.runStep))
			else:
				pf.write(line)

		pf.close()


	def createJobScript(self):
		# create pbs job script (parallel run)
		pbsFile = _rundir + "job.pbs"
		pf = open(pbsFile, 'w')
		pbs = '''#!/bin/bash

#SBATCH --job-name=%s_c%d
#SBATCH -N %d
#SBATCH -n %d
#SBATCH --partition=%s
#SBATCH --no-requeue
#SBATCH --time=%d:00:00
#SBATCH --export=ALL

module load gcc
module add mvapich2/gcc

lammpsdir="%s"
mpirun -np %d $lammpsdir/lmp_openmpi -in in.chromosome
'''%(self.celltype,self.chrId,self.nNode,self.ncpu,self.ptn,self.time,self.lmpsdir,self.ncpu)
		pf.write(pbs)
		pf.close()


	def createLocalBash(self):
		# create local bash script (serial run)
		localtime = time.asctime( time.localtime(time.time()) )
		runFile = _rundir+"run.sh"
		pf = open(runFile, 'w')
		pbs = '''# ---- Chromosome simulation locally in serial ---- #
# ---- Created Time: %s ---- #

#!/bin/bash
%s/lmp_openmpi -in in.chromosome'''%(localtime,self.lmpsdir)
		pf.write(pbs)
		pf.close()

		_cmd = 'chmod 744 %s'%(runFile)
		q = Popen(_cmd, shell=True, stdout=PIPE)
		q.communicate()
