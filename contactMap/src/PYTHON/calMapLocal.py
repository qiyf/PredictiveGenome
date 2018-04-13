# calculate the cmap locally
from Ipt_module import *
from Params import *
Params()

def calMapLocal(celltype,runnum,chrom_lst):

	src_path = '%s/src/'%glb_path
	ipt_path = '../lammps_input/'

	for chromid in chrom_lst:
		for runid in xrange(runnum):
			dcd_path  = '%s/%s/%s/chr%d/run%02d/'\
						%(glb_path,ipt_path,celltype,chromid,runid)
			cmap_path = './%s/chr%d/run%02d/'\
						%(celltype,chromid,runid)

			if not os.path.exists(cmap_path):
				os.makedirs(cmap_path)
			fo = open('%s/cal_cmap.sh'%(cmap_path),'w')
			fo.writelines('''#!/bin/bash

%s/FORTRAN/cmap %s/DUMP_FILE.dcd %d %d %d %d'''\
		%(src_path,dcd_path,cg_fac,startb,endb,startfr))
			fo.close()

			cmd = 'cd %s;chmod 744 cal_cmap.sh;./cal_cmap.sh;'%(cmap_path)
			q = Popen(cmd, shell=True, stdout=PIPE)
			print('''
>>>> Calculating contact map of %s, chromosome %d, parallel running %d....
'''%(celltype,chromid,runid))
			q.communicate()
