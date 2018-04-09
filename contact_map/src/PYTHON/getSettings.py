import sys
import getopt

def getSettings(argv):

	try:
		opts,args = getopt.getopt(args,'hC:r:c:',\
								['Cell=','runnum=','chrom='])
