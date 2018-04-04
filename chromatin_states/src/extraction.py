#!/usr/bin/env python

import sys
import numpy as np
import fileinput as fi

def convert_to_raw(infile, outfile, chrId, res):

    chrom = 'chr%d'%chrId

    fo = open(outfile, 'w')
    for line in fi.input(infile):
        items = line.split()
        if items[0] == chrom:
            gsta = int(items[1])
            gend = int(items[2])

            for gp in range(gsta, gend, res):
                fo.write('%d %s\n'%(gp, items[3]))
    fo.close()