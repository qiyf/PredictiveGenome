import sys
import getopt

def getSettings(argv):
#	-------------------------------------------------------------------
#	This function is to obtain the settings for CTCF-binding processing
#	-------------------------------------------------------------------

#	---- default values ----
#
	Celltype = 'Gm12878';chrom_lst=[1];bind_flxb=100;cap=50;
#	------------------------

	try:
		opts,args = getopt.getopt(argv,'hC:c:b:p:',\
								['Cell=','chrom=','bindflex=','cap='])
		for opt,arg in opts:
			if opt=='-h':
				print('''
>>>> Options: processingCTCF.py -C <Celltype> -c <chromosome id> -b <binding flexbility> -p <CTCF-cohesin nearest dist>
          or: processingCTCF.py --Cell <Celltype> --chrom <chromosome id> --bindflex <binding flexbility> --cap <CTCF-cohesin nearest dist>
''')
				sys.exit()
			elif opt in ('-C','--Cell'):
				Celltype = arg
			elif opt in ('-c','--chrom'):
				chrom1st	= [int(arg)]
				chrom2te	= map(eval, args)
				chrom_lst	= chrom1st+chrom2te
			elif opt in ('-b','--bindflex'):
				bind_flxb = arg
			elif opt in ('-p','--cap'):
				cap = arg

		print("Calculating CTCF-binding sites of %s ......"%Celltype)
		return Celltype,chrom_lst,bind_flxb,cap

	except getopt.GetoptError:
		print('''
>>>> Default setting is GM12878, chromosome 1, motif matching buffer 100bp, CTCF-cohesin nearest distance 50bp.
>>>> To see the manual and change the settings:
     type: processingCTCF.py -h 
''')


def getMotifSettings(argv):
#	------------------------------------------------------------
#	This function is to obtain the settings for motif processing
#	------------------------------------------------------------

#	---- default values ----
#
	motif_fi = 'hg19.motifs.txt';chrom_lst=[1];option='lbm';
#	------------------------

	try:
		opts,args = getopt.getopt(argv,'hm:c:p:',\
								['motif=','chrom=','option='])
		for opt,arg in opts:
			if opt=='-h':
				print('''
>>>> Options: prepareMotif.py -m <motif_name> -c <chromosome id> -p <motif_folder_name_option>
          or: prepareMotif.py -motif <motif_name> -chrom <chromosome id> -option <motif_folder_name_option>
''')
				sys.exit()
			elif opt in ('-m','--motif'):
				motif_fi = arg
			elif opt in ('-c','--chrom'):
				chrom1st	= [int(arg)]
				chrom2te	= map(eval, args)
				chrom_lst	= chrom1st+chrom2te
			elif opt in ('-p','--option'):
				option = arg

		print("Preprocessing the motif file: %s ......"%motif_fi)
		return motif_fi,chrom_lst,option

	except getopt.GetoptError:
		print('''
>>>> To see the manual and change the settings:
     type: prepareMotif.py -h 
''')
