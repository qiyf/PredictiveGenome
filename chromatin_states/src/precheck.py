#!/usr/bin/env python

import sys
import numpy as np
import fileinput as fi

def checkcell(celltype0):

    cellList = [\
'Gm12878',\
'H1hesc',\
'Helas3',\
'Hepg2',\
'Huvec',\
'K562']
    flag = 1
    celltype = celltype0
    if celltype0 not in cellList:
        flag = 0
        print('\n[WARNING]: Please recheck the README about the available cell types....\n')
    elif celltype0 == 'Helas3':
        celltype = 'Hela'

    return flag,celltype