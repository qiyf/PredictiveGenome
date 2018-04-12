from Ipt_module import *
from Params import *
Params()

def extractMotif(motif_type,chrId):
#
#	----	this function is to extract the pre-processed motif file
# 
	motif_name = '%s/motif_file/motif_%s/motif_chr%d.txt'\
					%(glb_path,motif_type,chrId)

	orientation_list = []
	for lines in fi.input(motif_name):
		every_line = lines.split()
		orientation_list.append([every_line[0],every_line[1]])
	return orientation_list
