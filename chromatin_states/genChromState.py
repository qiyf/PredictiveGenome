# generate chromatin states from Epigenetic data
import sys
sys.path.append('./src/')
from Ipt_module import *
from Params import *
Params()

from getSettings import getSettings
from Extraction import *
from precheck import checkcell


if __name__=='__main__':

    celltype,chrom_lst=getSettings(sys.argv[1:])
    Extn = Extraction()

    try:
        for chrId in chrom_lst:
            Extn.convert2raw(celltype, chrId)
            Extn.raw2state(celltype, chrId)
            print('''
>>>> Successfully generate: %s, chromosome %d
     located in the path: \'./model_input/%s/\'.
'''%(celltype,chrId,celltype))

    except IOError:
		print('''
>>>> [Warning] Error in calculating chromatin states of %s!
               Please check the README file for detail.
'''%celltype)
