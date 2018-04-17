# output the reads of certain resolutions
import sys
sys.path.append('../src/')
from Ipt_module import *
from Params import *
Params()

from assitingfunc import *
from preprocessingNarrowPeak import prepNarrowPeak

if __name__ == '__main__':

	#
	# ---- input settings ----
	#	
	celltype,tf,chrom_lst=getNarrowPeakSettings(sys.argv[1:])

	for chrId in chrom_lst:
		try:
			raw_data = './narrowPeak/%s_%s.narrowPeak'%(celltype,tf)
			raw_mat = np.genfromtxt(raw_data,dtype = 'str',comments = '@',usecols=(0,1,2))

			to_path = './%s/%s/'%(celltype,tf)
			if not os.path.exists(path):
				os.makedirs(path)

			fw = '%s/chip-seq_peak_%d.txt'%(path,chrId)
			write_in(raw_mat,fw)
			print('''   > %s, %s is completed!'''%(celltype,tf))

		except IOError:
			print('''
>>>> [WARNING]: Error in calculating narrow peaks of %s, chromosome %d!
	            Please recheck the README file for detail.'''%(celltype,chrId))
	print