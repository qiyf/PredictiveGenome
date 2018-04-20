# generate VMD scripts
import sys
sys.path.append('./VMDScript/')
from getSettings import getSettings
from genVMDScript import *

if __name__ == '__main__':

	# ---- input settings ---- #
	celltype,chrom_lst = getSettings(sys.argv[1:])

	# ---- generate individual VMD scripts ---- #
	for chrId in chrom_lst:
		genVMDScript(celltype,chrId)
	print