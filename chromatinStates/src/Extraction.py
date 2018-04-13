# convert the ChromHMM output
from Ipt_module import *
from Params import *
Params()

class Extraction():

	# ----    Global path 	----
	_cs_folder = 'OUTPUTSAMPLE_5kb_6celltype_15states'
	_csdir = '%s/raw_data/%s/'%(glb_path,_cs_folder)
	_csfile = ''
	_todir = ''


	def convert2raw(self,celltype,chrId):
	# ----    raw output from ChromHMM    ----
		infile = self._csdir+celltype+'_15_segments.bed'

		#   ----    raw State processed folder  ----
		global _todir
		_todir = '%s/model_input/%s/'%(glb_path,celltype)
		todirraw = _todir+'rawStates/'
		if os.path.exists(todirraw) is not True and flag:
			os.makedirs(todirraw)

		#   ----    raw State processed file    ----
		global _csfile
		_csfile = '%s/%s_chr%d_chromatin_states_raw.txt'%(todirraw,celltype,chrId)

		#   ----    generate raw State file     ----       
		fo = open(_csfile, 'w')
		for line in fi.input(infile):
			items = line.split()
			if items[0] == 'chr%d'%chrId:
				gsta = int(items[1])
				gend = int(items[2])
				for gp in range(gsta, gend, resolution):
					fo.write('%d %s\n'%(gp, items[3]))
		fo.close()


	def raw2state(self,celltype,chrId,realPos=False):
	#   ----    Chromatin state file name     ----
		outfile = '%s/%s_chr%d_chromatin_states.txt'%(_todir,celltype,chrId)
		csta = chr_region[chrId-1,1] * Mb +1
		cend = chr_region[chrId-1,2] * Mb

		#   ----    generate chrom state file     ---- 
		fo = open(outfile, 'w')
		for line in fi.input(_csfile):
			items = line.split()
			gpos = int(items[0])
			#   ----    output the absolute position  ---- 
			if gpos >=csta and gpos <= cend:
				if realPos:
					fo.write('%8d %4d\n'%(gpos, int(items[1][1::])))
				else:
					fo.write('%8d %4d\n'%((gpos-csta)/resolution+1,\
											int(items[1][1::])))
		fo.close()

