# generate the job script and submit the job
from Ipt_module import *
from Params import *
Params()

def proc(celltype,chromid,runid,job_name,ptn_name):

	glb_path  = '../lammps_input/run_folder'
	dcd_path  = '%s/%s/chr%d/run%02d/'\
				%(glb_path,celltype,chromid,runid)
	cmap_path = './%s/chr%d/run%02d/'\
				%(celltype,chromid,runid)

	if not os.path.exists(cmap_path):
		os.makedirs(cmap_path)
	fo = open('%s/job_cg.pbs'%(cmap_path),'w')
	fo.writelines('''#!/bin/bash

#SBATCH --job-name=%s
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=%s
#SBATCH --mem-per-cpu=2G
#SBATCH --time=4:00:00
#SBATCH --export=ALL

./src/FORTRAN/cmap %s/DUMP_FILE.dcd %d %d %d %d'''\
%(job_name,ptn_name,dcd_path,cg_fac,startb,endb,startfr))
	fo.close()

	cmd = 'cd %s;sbatch job_cg.pbs;'%(cmap_path)
	q = Popen(cmd, shell=True, stdout=PIPE)
	q.communicate()