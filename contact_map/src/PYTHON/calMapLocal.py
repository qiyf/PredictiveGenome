# calculate the cmap locally
from Ipt_module import *
from Params import *
Params()

def proc_local(celltype,chromid,runid):

	glb_path  = '../lammps_input/run_folder/'
	dcd_path  = '%s/%s/chr%d/run%02d/'\
				%(glb_path,celltype,chromid,runid)
	cmap_path = './%s/chr%d/run%02d/'\
				%(celltype,chromid,runid)

	if not os.path.exists(cmap_path):
		os.makedirs(cmap_path)
	fo = open('%s/cal_cmap.sh'%(cmap_path),'w')
	fo.writelines('''#!/bin/bash
./src/FORTRAN/cmap %s/DUMP_FILE.dcd %d %d %d %d'''\
%(job_name,ptn_name,dcd_path,cg_fac,startb,endb,startfr))
	fo.close()

	cmd = 'cd %s;chmod 744 cal_cmap.sh;./cal_cmap.sh;'%(cmap_path)
	q = Popen(cmd, shell=True, stdout=PIPE)
	q.communicate()