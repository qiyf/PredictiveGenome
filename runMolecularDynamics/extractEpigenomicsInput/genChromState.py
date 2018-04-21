# generate chromatin states from Epigenetic data
import sys
sys.path.append('../../src/')

from chromatinState import *


if __name__=='__main__':

    # ---- input settings ---- #
    celltype,chrom_lst=getSettings(sys.argv[1:])

    print celltype

    cs = chromatinState()

    # ---- two-step extraction ---- #
    for chrId in chrom_lst:
        cs.celltype = celltype
        cs.chrId = chrId
        cs.convert2raw()
        cs.raw2state()
    try:
        for chrId in chrom_lst:
            cs.celltype = celltype
            cs.chrId = chrId
            cs.convert2raw()
            cs.raw2state()
    except IOError:
		print('''
>>>> [Warning] Error in calculating chromatin states of %s!
     Please check the README file for detail.'''%celltype)
    print
