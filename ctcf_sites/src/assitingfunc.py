from Ipt_module import *

def process_minabs(ctcfPos,rad21_peaks):
#
#	----	this function is to find the nearest radPos to each ctcf	----
#
	radPos = rad21_peaks[0][0]
	radPos_min = radPos
	dist_min = abs(radPos-ctcfPos)

	for i in range(len(rad21_peaks)):
		radPos = 0.5*(rad21_peaks[i][0]+rad21_peaks[i][1])
		dist = abs(radPos-ctcfPos)

		if dist <= dist_min:
			dist_min = dist
			radPos_min = radPos

	return radPos_min


def update_cs_type(org,ext):
#
#	----	update the chromatin state	----
#
	if org == 4 or ext == 4:
		upd = 4
	elif org == 0 or ext == 0:
		upd = 4
	elif ( org == 1 and ext == 2 ) or ( org == 2 and ext == 1 ):
		upd = 4
	elif org == 1 and ext == 1:
		upd = 1
	elif org == 2 and ext == 2:
		upd = 2
	return upd


def write_in(raw_mat,write_in_file):
#
#	----	write in the matrix in the original form	----
#
	pf = open(write_in_file,'w')
	region = extract_interval(raw_mat,chrid)

	for i in range(len(region)):
		for j in range(2):
			pf.writelines(region[i][j])
			pf.writelines('\t')
		pf.writelines('\n')
	pf.close()