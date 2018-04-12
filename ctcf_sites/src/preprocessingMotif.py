from Ipt_module import *
from Params import *
Params()

def prepMotif(file_name, chrid):

	all_chr = []
	orientation_list = []
	start = chr_region[chrid-1][0]*Mb
	end = chr_region[chrid-1][1]*Mb

	for lines in fi.input(file_name):
		every_line = lines.split()
		if  every_line[1] == '%d'%chrid \
		and int(every_line[2]) >= start \
		and int(every_line[3]) <= end:
			temp = []
			temp.append(every_line[2])		# starting position
			temp.append(every_line[4])		# orientation
			orientation_list.append(temp)	# with orientations as '+' or '-'

	return orientation_list
