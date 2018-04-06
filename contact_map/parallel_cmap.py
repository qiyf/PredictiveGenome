# build up parallel simulations for calculation of cmaps
import sys
sys.path.append('./src/PYTHON/')
from Ipt_module import *
from Params import *
Params()
from processingJobScript import proc
from checkStatus import check_status
from combineMaps import combine_cmaps


if __name__ == '__main__':

	if len(sys.argv) == 1:
		celltype = 'Gm12878'
		runnum = 8
		chrom_lst = [1]
	else:
		celltype = sys.argv[1]
		runnum = int(sys.argv[2])
		chrom_lst = sys.argv[3:]
		chrom_lst = map(eval, chrom_lst)

	job_name = 'cmap'										# name of the jobs running cmaps
	ptn_name = 'sched_mit'									# name of the partition name
															# need to be changed accordingly

	for chromid in chrom_lst:
		for runid in xrange(runnum):
			processingJobScript(celltype,chromid,runid,job_name,ptn_name)
															# prepare the job script for calculating cmaps
	check_status()											# check the job status

	for chromid in chrom_lst:
		combine_cmaps(celltype,chromid,runnum)		# combine the parallel cmaps to ensemble average

