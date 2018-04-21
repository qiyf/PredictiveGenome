# generate chromatin states from Epigenetic data
import sys
sys.path.append('../../src/')

from chromatinState import *

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
                                chrom1st        = [int(arg)]
                                chrom2te        = map(eval, args)
                                chrom_lst       = chrom1st+chrom2te
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
