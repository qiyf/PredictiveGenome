#!/usr/bin/env python

import sys
import numpy as np
import fileinput as fi

def genState(infile, outfile, chrId,res, csta, cend, realPos=False):

    chrom = 'chr%d'%chrId

    fo = open(outfile, 'w')
    for line in fi.input(infile):
        items = line.split()
        gpos = int(items[0])

        if gpos >=csta and gpos <= cend:

            if realPos:
                fo.write('%8d %4d\n'%(gpos, int(items[1][1::])))
            else:
                fo.write('%8d %4d\n'%((gpos-csta)/res+1, int(items[1][1::])))

    fo.close()
