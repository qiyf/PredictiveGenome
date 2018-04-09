# build up parallel simulations for calculation of cmaps
import sys
sys.path.append('./src/PYTHON/')
from Ipt_module import *
from Params import *
Params()
from Settings import *
Settings()

from getSettings import getSettings
from processingJobScript import proc
from checkStatus import check_status
from combineMaps import combine_cmaps


if __name__ == '__main__':

	if len(sys.argv) == 1: pass								# go with the default settings
	else:
		# celltype = sys.argv[1]
		# runnum = int(sys.argv[2])
		# chrom_lst = sys.argv[3:]
		# chrom_lst = map(eval, chrom_lst)
		celltype,runnum,chromid=\
						getSettings(sys.argv[1:])

	print(chromid)
	clus_opt=raw_input("\nComputing clusters available?[y/n] ")
	if clus_opt == 'y':
		# job_name = 'cmap'									# name of the jobs running cmaps
		ptn_name = raw_input('Input the partition name: ')		# name of the partition name
															# need to be changed accordingly
		# for chromid in chrom_lst:
		# 	for runid in xrange(runnum):
		# 		processingJobScript(celltype,chromid,runid,job_name,ptn_name)
		# 														# prepare the job script for calculating cmaps
		# check_status()											# check the job status

	else:
		calMapLocal(celltype,chromid,runid)

	for chromid in chrom_lst:
		combine_cmaps(celltype,chromid,runnum)		# combine the parallel cmaps to ensemble average

