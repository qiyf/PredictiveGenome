# build up parallel simulations
import os
from subprocess import *
import fileinput as fi
import numpy as np
import time
import sys

cg_fac = 10
num_kb = 5*cg_fac
startb = 400
endb = 4400
startfr = 1
nbead_cg = int(5000/cg_fac*0.8)


def proc(chromid,iterid,runid):

	dcd_path = '../lammps_input/chr%d/iter%02d/run%02d/'
	if not os.path.exists('./chr%d/iter%03d_%dkb/run%02d/'%(chromid,iterid,num_kb,runid)):
		os.makedirs('./chr%d/iter%03d_%dkb/run%02d/'%(chromid,iterid,num_kb,runid))
	fo = open('./chr%d/iter%03d_%dkb/run%02d/job_cg.pbs'%(chromid,iterid,num_kb,runid),'w')
	fo.writelines('''#!/bin/bash

#SBATCH --job-name=py_chip-seq
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --partition=sched_mit_binz
#SBATCH --exclude=node[001-289]
#SBATCH --mem-per-cpu=2G
##SBATCH --gres=gpu:1
#SBATCH --time=12:00:00
#SBATCH --export=ALL

./src/cmap %s/DUMP_FILE.dcd %d %d %d %d'''%(dcd_path,cg_fac,startb,endb,startfr))
	fo.close()

	cmd = 'cd ./chr%d/iter%03d_%dkb/run%02d/;sbatch job_cg.pbs;'%(chromid,iterid,num_kb,runid)
	q = Popen(cmd, shell=True, stdout=PIPE)
	q.communicate()

def check_status():

	njob = -1
	while True:
		cmd = 'squeue |grep qiyf |grep py_chip |wc -l'
		q = Popen(cmd, shell=True, stdout=PIPE)
		njob = int(q.communicate()[0])
		print (njob)
		if njob == 0:
			break
		else:
			time.sleep(10)

def combine_contact_map(chromid,iterid,runnum):
	combine = np.zeros([nbead_cg,nbead_cg])
	nf_tot = 0
	if os.path.exists('./chr%d/iter%03d_%dkb/run00/contact_map_CG.txt'%(chromid,iterid,num_kb)):
		for run_id in range(0,runnum):
			in_temp = np.loadtxt('./chr%d/iter%03d_%dkb/run%02d/contact_map_CG.txt'%(chromid,iterid,num_kb,run_id))
			nf = np.loadtxt('./chr%d/iter%03d_%dkb/run%02d/nframes.txt'%(chromid,iterid,num_kb,run_id))

			combine += in_temp*nf
			nf_tot += nf

		combine /= nf_tot
		np.savetxt('./cmap_comb_%dkb/contact_map_CG_comb_chr%d_iter%d.txt'%(num_kb,chromid,iterid),combine,fmt = '%.8f')
		print('contact_map_CG_%d is combined sucessfully!'%chromid)
	else:
		print('Error in combining the contact maps of chromosome %d!'%chromid)

if __name__ == '__main__':

	iterid = int(sys.argv[1])
	runnum = int(sys.argv[2])
	arraynum = int(sys.argv[3])

	num_arg = len(sys.argv)
	chrom_lst = []
	for arg_id in xrange(4,num_arg):
		chrom_lst.append(int(sys.argv[arg_id]))

	for chromid in chrom_lst:
		for runid in xrange(runnum):
			link_dcd(chromid,iterid,runid,arraynum)

	for chromid in chrom_lst:
		for runid in xrange(runnum):
			proc(chromid,iterid,runid)

	check_status()
	for chromid in chrom_lst:
		combine_contact_map(chromid,iterid,runnum)

