# build up parallel simulations for calculation of cmaps
import sys
sys.path.append('./src/PYTHON/')
from Ipt_module import *
from Params import *
Params()
from Settings import *
Settings()

from getSettings import getSettings
from processingJobScript import *
from calMapLocal import calMapLocal
from checkStatus import checkStatus
from combineMaps import combineMaps


if __name__ == '__main__':

	celltype,runnum,chrom_lst=getSettings(sys.argv[1:])						# settings
	clus_opt=raw_input("Computing clusters available?[y/n] ")				# Cluster computing or locally
	
	if clus_opt == 'y':
		job_name = 'cmap'													# name of the jobs running cmaps
		usr_name = raw_input('Input cluster user name: ')					# user name on the cluster
		ptn_name = raw_input('Input the partition name: ')					# input partition name if cluster available 
		processingJobScript(celltype,runnum,chrom_lst,job_name,ptn_name)	# prepare the job script for calculating cmaps
		checkStatus(usr_name,job_name)										# check the job status
	else:
		calMapLocal(celltype,runnum,chrom_lst)								# calculate the cmap locally

	for chromid in chrom_lst:
		combineMaps(celltype,runnum,chromid)								# combine the parallel cmaps to ensemble average
