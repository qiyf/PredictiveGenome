from Ipt_module import *

def extract_motif_orientation(file_name):
#
#	----	this function is to extract the pre-processed motif file
# 
	orientation_list = []
	for lines in fi.input(file_name):
		every_line = lines.split()
		orientation_list.append([every_line[0],every_line[1]])
	return orientation_list
