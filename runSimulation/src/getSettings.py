import sys
import getopt

def getSettings(argv):
#
# ---- default values ----
	Celltype = 'Gm12878';chrom_lst=[1];runnum=8;
	nNode=1;ncpu=14;ptn='sched_mit_binz';time=48;lmpsdir='../LAMMPS-PreGenome/src/';
	ctcfthres=4;step=40000000;
# ------------------------

	try:
		opts,args = getopt.getopt(argv,'hC:c:n:N:p:i:t:l:d:r:',\
								['Cell=','chrom=','runnum=','nNode=','ncpu','ptn','time','lmpsdir','ctcfthres','step'])
		for opt,arg in opts:
			if opt=='-h':
				print('''
>>>> Options: parallel_cmap.py -C <Celltype> -c <chromosome id> -n <run number> -N <number of Node> -p <number of cpu> 
							   -i <partition> -t <simulation time> -l <Lammps dir> -d <near CTCF threshold> -r <simulation steps>
		  or: parallel_cmap.py --Cell <Celltype> --chrom <chromosome id> --runnum <run number> --nNode <number of Node> --ncpu <number of cpu> 
							   --ptn <partition> --time <simulation time> --lmpsdir <Lammps dir> --ctcfthres <near CTCF threshold> --step <simulation steps>
''')
				sys.exit()
			elif opt in ('-C','--Cell'):
				Celltype = arg
			elif opt in ('-c','--chrom'):
				chrom1st	= [int(arg)]
				chrom2te	= map(eval, args)
				chrom_lst	= chrom1st+chrom2te
			elif opt in ('-n','--runnum'):
				runnum = int(arg)
			elif opt in ('-N','--nNode'):
				nNode = int(arg)
			elif opt in ('p','--ncpu'):
				ncpu = int(arg)
			elif opt in ('-i','--ptn'):
				ptn = arg
			elif opt in ('-t','--time'):
				time = int(arg)
			elif opt in ('-l','--lmpsdir'):
				lmpsdir = arg
			elif opt in ('-d','--ctcfthres'):
				ctcfthres = int(arg)
			elif opt in ('-r','--step'):
				step = int(arg)

	except getopt.GetoptError:
		print('''
>>>> [Warning] Error in intializing the simulation!
>>>> To see the manual and change the settings:
	 type: parallel_cmap.py -h 
''')

	return Celltype,chrom_lst,runnum,nNode,ncpu,ptn,time,lmpsdir,ctcfthres,step
