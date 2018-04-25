#!/usr/bin/env python
import sys
sys.path.append('../src/md/')
from Ipt_module import *
from Params import *

from getSettings import getSettings
from CreateLAMMPSFile import *

if __name__ == '__main__':

	# ---- input settings ---- #
	celltype,runnum,\
	nNode,ncpu,ptn,simtime,lmpsdir,\
	nearCtcfThreshold,runStep,\
	bind_flxb,cap,\
		chrom_lst=getSettings(sys.argv[1:])

	# ---- cluster computing or locally ---- #

	for chrId in chrom_lst:
		for runId in xrange(runnum):
			Clf=CreateLAMMPSFile(celltype,chrId,runId,\
								nNode,ncpu,ptn,simtime,lmpsdir,\
									nearCtcfThreshold,runStep)
			Clf.createLAMMPSDataFile()
			Clf.createLAMMPSInputFile()
			Clf.createLocalBash()
	print
