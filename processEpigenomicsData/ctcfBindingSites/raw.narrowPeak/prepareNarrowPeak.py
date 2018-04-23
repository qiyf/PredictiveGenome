import sys
sys.path.append('../../../../src/ctcf/')
from Ipt_module import *

from getSettings import getNarrowPeakSettings
from preprocessing import prepNarrowPeak
from writeinfunc import *

if __name__ == '__main__':

	# ---- input settings ---- #
	celltype,tf,chrom_lst=getNarrowPeakSettings(sys.argv[1:])

	for chrId in chrom_lst:
		try:
			raw_data = './narrowPeak/%s_%s.narrowPeak'%(celltype,tf)
			raw_mat = np.genfromtxt(raw_data,dtype = 'str',comments = '@',usecols=(0,1,2))
			region = prepNarrowPeak(raw_mat,chrId)
			writein_2d(celltype,tf,chrId,region)
			print('''   > %s, %s is completed!'''%(celltype,tf))

		except IOError:
			print('''
>>>> [WARNING]: Error in calculating narrow peaks of %s, chromosome %d!
                Please recheck the README file for detail.'''%(celltype,chrId))
	print
