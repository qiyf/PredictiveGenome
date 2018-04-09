import sys
import getopt

def getSettings(argv):

	try:
		opts,args = getopt.getopt(argv,'hC:n:c:',\
								['Cell=','runnum=','chrom='])
	except getopt.GetoptError:
		print('''
>>>> Error: parallel_cmap.py -C <Celltype> -n <run number> -c <chromosome id>
        or: parallel_cmap.py --Cell <Celltype> --runnum <run number> --chrom <chromosome id>

      type: parallel_cmap.py -h 
      		to see the manual.''')
		sys.exit(2)

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
			chromid = int(arg)

	return Celltype,runnum,chromid
