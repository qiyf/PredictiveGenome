from Ipt_module import *
chr_region=np.loadtxt('../../../../src/chr_region.txt')
Mb=1E6


def prepMotif(file_name, chrId):
#	----	This function is to pre-process the motif file 	---- #

	all_chr = []
	oriList = []
	start = chr_region[chrId-1][0]*Mb
	end = start+25*Mb

	for lines in fi.input(file_name):
		every_line = lines.split()
		if  every_line[1] == '%d'%chrId \
		and int(every_line[2]) >= start \
		and int(every_line[3]) <= end:
			temp = []
			temp.append(every_line[2])		# starting position
			temp.append(every_line[4])		# orientation
			oriList.append(temp)			# with orientations as '+' or '-'
	return oriList


def prepNarrowPeak(raw_mat,chrId):
#	----	This function is to pre-process the narrow peak file 	---- #

	shift = 0
	start = chr_region[chrId-1][0]*Mb
	end = start+25*Mb
	region = []

	for i in range(len(raw_mat)):
		if raw_mat[i][0] == 'chr%d'%(chrId) \
			and int(raw_mat[i][1])>=(start-shift) \
			and int(raw_mat[i][2])<=(end+shift):
			region.append([raw_mat[i][1],raw_mat[i][2]])

	return region
