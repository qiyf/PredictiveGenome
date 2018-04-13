import sys
import numpy as np
sys.path.append('../src/')

from getSettings import getMotifSettings
from preprocessingMotif import prepMotif
from assitingfunc import *


if __name__ == '__main__':
#
#	----	extract the motif information with the start position and orientation
#
    # ---- input settings ----
    motif_fi,chrom_lst,option=getMotifSettings(sys.argv[1:])

	try:
		oriList = prepMotif(motif_fi,chrId)
		writein_motif(chrId,option,oriList)

	except IOError:
		print('''
>>>> [WARNING]: Error in preprocessing the motif files!
                Please provide a valid raw motif file, see README for detail, or to use the existing motif files to process.
''')
