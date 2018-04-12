from Ipt_module import *
from Params import *
Params()

def extract_interval(raw_mat,chromid):

	shift = 0
	startid = chr_region[chromid-1][1]*Mb
	endid = chr_region[chromid-1][2]*Mb
	region = []

	for i in range(len(raw_mat)):
		if raw_mat[i][0] == 'chr%d'%(chromid) \
			and int(raw_mat[i][1])>=(startid-shift) \
			and int(raw_mat[i][2])<=(endid+shift):
			region.append([raw_mat[i][1],raw_mat[i][2]])

	return region
