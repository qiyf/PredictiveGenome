#!/usr/bin/env python

import sys
import os
import numpy as np
import fileinput as fi
sys.path.append('./src/')
from extraction import convert_to_raw
from genStates import genState
from precheck import checkcell


if __name__=='__main__':

    chr_region = np.loadtxt('../chr_region.txt')
    res = 5000
    Mb = 1000000

    if len(sys.argv) == 1: celltype0 = 'Gm12878'; chrId = 1
    else: celltype0 = sys.argv[1]; chrId = int(sys.argv[2])
    flag,celltype = checkcell(celltype0)

    csdir = './raw_data/OUTPUTSAMPLE_5kb_6celltype_15states/'
    infile = csdir + celltype0 + '_15_segments.bed'

    csta = chr_region[chrId-1,1] * Mb +1
    cend = chr_region[chrId-1,2] * Mb

    todir = './model_input/%s/'%(celltype)
    todirraw = todir+'rawStates/'

    try:
    	if os.path.exists(todirraw) is not True and flag:
	        os.makedirs(todirraw)
        csfile = '%s/%s_chr%d_chromatin_states_raw.txt'%(todirraw,celltype,chrId)
        convert_to_raw(infile, csfile, chrId, res)
        outfile = '%s/%s_chr%d_chromatin_states.txt'%(todir,celltype,chrId)
        genState(csfile, outfile, chrId, res, csta, cend)
        print('''\n>>>> Successfully generate: %s, chromosome %d
     located in the path: \'./model_input/%s/\'.\n'''%(celltype,chrId,celltype))

    except IOError:
		pass
