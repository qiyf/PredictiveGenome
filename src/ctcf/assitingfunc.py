from Ipt_module import *
from Params import *
Params()

def process_minabs(ctcfPos,rad21_peaks):

#	----	find the nearest radPos to each ctcf	---- #
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

#	----	update the chromatin state	---- #
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


def writein_2d(to_path,to_path_file,writeinfile):

#	----	templating the writing of a 2d matrix	---- #
	if not os.path.exists(to_path):
		os.makedirs(to_path)
	fw = open(to_path+to_path_file,'w')
	for ii in xrange(len(writeinfile)):
		fw.writelines(str(int(writeinfile[ii][0]))+'\t'\
						+str(int(writeinfile[ii][1]))+'\n')
	fw.close()


def writein_ctcf(celltype,chrId,cap,writeinfile):

#	----	write in the matrix in the original form	---- #
	staid = chr_region[chrId-1,1]
	endid = chr_region[chrId-1,2]
	to_path = '%s/processedCTCF/proc_data.%dbp/%s/'%(glb_path,cap,celltype)
	to_path_file = '%s_chr%d_ctcf_%dMbTo%dMb.txt'%(celltype,chrId,staid,endid)
	writein_2d(to_path,to_path_file,writeinfile)


def writein_motif(chrId,opt,writeinfile):

#	----	write in the motif orientation file		---- #
	to_path = '%s/motif_%s/'%(glb_path,opt)
	to_path_file = 'motif_chr%d.txt'%chrId
	writein_2d(to_path,to_path_file,writeinfile)
	