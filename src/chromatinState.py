import random
import numpy as np
from scipy import stats
import scipy.io as scio 
import os
import time
import fileinput as fi
from math import *
from subprocess import *


import sys
import getopt

class chromatinState(object):
    '''
    extract chromatin states for lammps simulation.
    '''

    def __init__(self, celltype=None, chrId=None):
	
	# ---- default: 25Mb segment, at resolution of 5kb ---- #
	self.Mb=1E6
	self.resolution=5000

	self.nbead=25*self.Mb/self.resolution

        if celltype:
            self.celltype = celltype
        else:
            self.celltype = 'Gm12878'

        if chrId:
            self.chrId = chrId
        else:
            self.chrId = 1

	# ----    Global path 	---- #
	self.glb_path = os.getcwd()
	self._cs_folder = 'OUTPUTSAMPLE_5kb_6celltype_15states'
	self._csdir = '../../processEpigenomicsData/chromatinStates/%s/'%(self._cs_folder)
	self._csfile = ''
	self._todir = ''

	## ---- default: global path ---- #

	## ---- chromosome segment region ---- #
	self.chr_region = np.loadtxt('%s/../runSimulation/chr_region.txt'%self.glb_path)

    def convert2raw(self):
	# ----    raw output from ChromHMM    ---- #
        infile = self._csdir+self.celltype+'_15_segments.bed'
        
        #   ----    raw State processed folder  ---- #
        self._todir = '%s/chromStates/%s/'%(self.glb_path,self.celltype)
        todirraw = self._todir+'rawStates/'
        if os.path.exists(todirraw) is not True:
        	os.makedirs(todirraw)
        
        #   ----    raw State processed file    ---- #
        self._csfile = '%s/%s_chr%d_chromatin_states_raw.txt'%(todirraw,self.celltype,self.chrId)
        
        #   ----    generate raw State file     ---- #     
        fo = open(self._csfile, 'w')
        for line in fi.input(infile):
        	items = line.split()
        	if items[0] == 'chr%d'%self.chrId:
        		gsta = int(items[1])
        		gend = int(items[2])
        		for gp in range(gsta, gend, self.resolution):
        			fo.write('%d %s\n'%(gp, items[3]))
        fo.close()


    def raw2state(self,realPos=False):
        #   ----    Chromatin state file name     ---- #
	staid = self.chr_region[self.chrId-1,1]
	endid = self.chr_region[self.chrId-1,2]
	csta = staid * self.Mb +1
	cend = endid * self.Mb
	outfile = '%s/%s_chr%d_chromatin_states_%dMbTo%dMb.txt'\
							%(self._todir,self.celltype,self.chrId,staid,endid)

	#   ----    generate chrom state file     ---- #
	fo = open(outfile, 'w')
	for line in fi.input(self._csfile):
		items = line.split()
		gpos = int(items[0])
		#   ----    output the absolute position  ---- #
		if gpos >=csta and gpos <= cend:
			if realPos:
				fo.write('%8d %4d\n'%(gpos,int(items[1][1::])))
			else:
				fo.write('%8d %4d\n'%((gpos-csta)/self.resolution+1,\
										int(items[1][1::])))
	fo.close()
	print('''   > Chromatin state for %s, chromosome %d is successfully generated.'''\
																	%(self.celltype,self.chrId))

def getSettings(argv):

# ---- default values ---- #
	Celltype = 'Gm12878';chrom_lst=[1];
# ------------------------ #
	
	try:
		opts,args = getopt.getopt(argv,'hC:c:',\
								['Cell=','chrom='])
		for opt,arg in opts:
			if opt=='-h':
				print('''
>>>> Options: genChromState.py -C <Celltype> -c <chromosome id>
          or: genChromState.py --Cell <Celltype> --chrom <chromosome id>
''')
				sys.exit()
			elif opt in ('-C','--Cell'):
				Celltype = arg
			elif opt in ('-c','--chrom'):
				chrom1st	= [int(arg)]
				chrom2te	= map(eval, args)
				chrom_lst	= chrom1st+chrom2te
		print('''
>>>> Calculating chromatin states of %s ......'''%Celltype)
		return Celltype,chrom_lst

	except getopt.GetoptError:
		print('''
>>>> [Warning] Error in setting options.
   > To see the manual and change the settings:
     python genChromState.py -h
''')
		sys.exit()
