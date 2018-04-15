#!/usr/bin/env python
import sys
sys.path.append('./src/')
from Ipt_module import *
from Params import *
Params()

from getSettings import getSettings
from CreateLAMMPSFile import *
from submitJobs import *


if __name__ == '__main__':

	# ---- input settings ---- #
	celltype,chrom_lst,runnum,\
	nNode,ncpu,ptn,time,lmpsdir,\
		nearCtcfThreshold,runStep=getSettings(sys.argv[1:])

	# ---- cluster computing or locally ---- #
	clus_opt=raw_input("Computing clusters available?[y/n] ")

	for chrId in chrom_lst:
		for runId in xrange(runnum):
			# ---- prepare simulation files ---- #
			Clf=CreateLAMMPSFile(celltype,chrId,runId,\
								nNode,ncpu,ptn,time,lmpsdir,\
									nearCtcfThreshold,runStep)
			Clf.createLAMMPSDataFile()
			Clf.createLAMMPSInputFile()

			if clus_opt == 'y':
				# ---- create and submit the job to the cluster ---- #
				Clf.createJobScript()
				# submitJobs(celltype,chrId,runId)
				print('''
>>>> Job for %s, chromosome %d, parrallel running %02d is processed for submission.'''\
								%(celltype,chrId,runId))
			else:
				# ---- create the bash script to run locally ---- #
				Clf.createLocalBash()
				print('''
>>>> [Warning] The local simulation bash script is generated located at:
			   ./run_folder/%s/chr%d/run%02d/run.sh'''\
								%(celltype,chrId,runId))
