import sys
sys.path.append('./src/')
from Ipt_module import *
from Params import *
Params()

from getSettings import getSettings
from processingMotif import extractMotif
from processingCTCFori import processingCTCFori
from assitingfunc import *
from GenCTCFinput import *


if __name__ == '__main__':

	# ---- input settings ---- #
	celltype,chrom_lst,bind_flxb,cap=getSettings(sys.argv[1:])

	for chrId in chrom_lst:
		# ---- prepare ctcf motif ---- #
		orilst_lbm = extractMotif('lbm',chrId)
		orilst_known = extractMotif('known',chrId)
		orilst_disc = extractMotif('disc',chrId)

		try:
			# ---- process CTCF site decide with near cohesin ---- #
			# ---- and orientation decided according to motif ---- #
			final_ctcf_states = processingCTCFori(celltype,chrId,orilst_lbm,\
												orilst_known,orilst_disc,bind_flxb,cap)

			# ---- output the list of ctcf sites ---- #
			writein_ctcf(celltype,chrId,cap,final_ctcf_states)

			# ---- generate the complete list of ctcf index as input to the model ---- #
			GCInput = GenCTCFinput()
			GCInput.generate(celltype,chrId,cap)

			print('''>>>> CTCF-binding sites for %s, chromosome %d is successfully constructed.
'''%(celltype,chrId))

		except IOError:
			print('''>>>> [WARNING]: Error in calculating CTCF-binding sites of %s, chromosome %d!
     Please recheck the README file for detail.
'''%celltype,chrId)