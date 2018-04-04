# output the reads of certain resolutions

import os
import sys
import numpy as np
sys.path.append('../src/')
from assitingfunc import *
from preprocessingNarrowPeak import extract_interval

if __name__ == '__main__':

	#
    # ---- input settings ----
    #	
	chr_region = np.loadtxt('../../chr_region.txt')
	tf = ['ctcf','rad21']

	if len(sys.argv) == 1: celltype='Gm12878'; chrId=1;
	else: celltype=sys.argv[1]; chrId=int(sys.argv[2]);
	try:
		for tf_type in tf:
			raw_data = '../../raw.narrowPeak/narrowPeak/%s_%s.narrowPeak'%(celltype,tf_type)
			raw_mat = np.genfromtxt(raw_data,dtype = 'str',comments = '@',usecols=(0,1,2))

			to_path = '../../raw.narrowPeak/%s/%s/'%(celltype,tf_type)
			if not os.path.exists(path):
				os.makedirs(path)

			fw = '%s/chip-seq_peak_%d.txt'%(path,chrId)
			write_in(raw_mat,fw)
			print('%s, %s is completed!'%(celltype,tf_type))

	except IOError:
		print('\n[WARNING]: Please recheck the README about the available cell types....\n')
