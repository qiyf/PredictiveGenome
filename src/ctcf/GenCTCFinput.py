from Ipt_module import *
from Params import *
Params()

from assitingfunc import *

class GenCTCFinput():

	def convert2sq(self,ctcf_path):
	#	----	processing into complete sequence	---- #
		tmp = np.loadtxt(ctcf_path)
		mat = np.zeros((nbead,2),dtype='int')
		for i in range(len(mat)):
			mat[i,0] = i+1
			mat[i,1] = 3
		
		for j in range(len(tmp)):
			mat[int(tmp[j][0])-1][1] = int(tmp[j][1])

		mat = mat.tolist()
		for i in range(len(mat)):
			mat[i][0] = int(mat[i][0])
			mat[i][1] = int(mat[i][1])
			if mat[i][1] == 0:
				mat[i][1] = 4
		return mat

	def extractCtcfConv(self,ctcfSeq):
	#	----	processing into CTCF index sequence	---- #
		ctcfL = []
		ctcfR = []
		ctcfInd = np.zeros((nbead,2),dtype='int')

		for ictcf in ctcfSeq:
			aid = int(ictcf[0])
			cs = int(ictcf[1])
			if (cs == 1):
				ctcfL.append(aid)
			elif (cs == 2):
				ctcfR.append(aid)
			elif (cs == 4):
				ctcfL.append(aid)
				ctcfR.append(aid)
			else:
				pass

		for aid in range(1, nbead+1):
			tmp = -1
			for cid in ctcfL:
				if cid <= aid:
					if cid > tmp:
						tmp = cid
				else:
					break
			if tmp == -1:
				ctcfInd[aid-1,0] = tmp
			else:
				ctcfInd[aid-1,0] = ctcfL.index(tmp)
			tmp = nbead+1
			for cid in ctcfR:
				if cid >= aid:
					if cid < tmp:
						tmp = cid
			if tmp <= nbead:
				ctcfInd[aid-1,1] = ctcfR.index(tmp)
			else:
				ctcfInd[aid-1,1] = -1

		return ctcfInd


	def generate(self,celltype,chrId,cap):
	#	----	generate the input data format for the model 	---- #
	#	----	common bead:3	CTCF+:1	CTCF-:2	CTCF+-:4 		---- #
		staid = chr_region[chrId-1,1]
		endid = chr_region[chrId-1,2]

		#	----	path to raw CTCF list
		to_path = '%s/processedCTCF/proc_data.%dbp/%s/'%(glb_path,cap,celltype)
		ctcf_path = '%s/%s_chr%d_ctcf_%dMbTo%dMb.txt'\
											%(to_path,celltype,chrId,staid,endid)

		#	----	path to input CTCF list (index)
		gen_path = '%s/../../runMolecularDynamics/runSimulation/'\
		'/input_files/epig_input/ctcfSites/%s/'%(glb_path,celltype)
		gen_path_file = 'ctcf_index_%s_chr%d_From%dMbTo%dMb.txt'\
												%(celltype,chrId,staid,endid)

		ctcfSeq = self.convert2sq(ctcf_path)
		ctcfInd = self.extractCtcfConv(ctcfSeq)

		#	----	write to path for output	---- #
		writein_2d(gen_path,gen_path_file,ctcfInd)
