import sys
import numpy as np
sys.path.append('../src/')
from preprocessingMotif import extract_orientation

if __name__ == '__main__':

	Mb = 1E6
	chr_region = np.loadtxt('../../chr_region.txt')

#
#	----	extract the motif information with the start position and orientation
#
	if len(sys.argv) == 1: motif_fi ='hg19.motifs.txt'; chrId = 1; opt = 'lbm'
	else: motif_fi = sys.argv[1]; chrId = int(sys.argv[2]); opt = sys.argv[3]

	try:
		orientation_list = extract_orientation(motif_fi,chrId)
		fw = open('./motif_%s/motif_chr%d.txt'%(opt,chrId),'w')
		for ii in xrange(len(orientation_list)):
			fw.writelines(orientation_list[ii][0]+'\t'+orientation_list[ii][1]+'\n')
		fw.close()

	except IOError:
		print('\n[WARNING]: Please provide a valid motif file, or use the existing files to process.\n')
