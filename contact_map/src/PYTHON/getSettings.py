import sys
import getopt

def getSettings(argv):
#
#	---- default values ----
#
	Celltype = 'Gm12878';runnum=8;chrom_lst=[1];
#	------------------------

	try:
		opts,args = getopt.getopt(argv,'hC:n:c:',\
								['Cell=','runnum=','chrom='])
		for opt,arg in opts:
			if opt=='-h':
				print('''
>>>> Options: parallel_cmap.py -C <Celltype> -n <run number> -c <chromosome id>
          or: parallel_cmap.py --Cell <Celltype> --runnum <run number> --chrom <chromosome id>
''')
				sys.exit()
			elif opt in ('-C','--Cell'):
				Celltype = arg
			elif opt in ('-n','--runnum'):
				runnum = int(arg)
			elif opt in ('-c','--chrom'):
				chrom1st	= [int(arg)]
				chrom2te	= map(eval, args)
				chrom_lst	= chrom1st+chrom2te

	except getopt.GetoptError:
		print('''
>>>> By default, calculate 8 parallel simulations of chromosome 1, GM12878.
>>>> To see the manual and change the settings:
     type: parallel_cmap.py -h 
''')

	return Celltype,runnum,chrom_lst
