import sys
sys.path.append('./src/')
from Ipt_module import *
from Params import *
Params()

from getSettings import getSettings
from processingMotif import extractMotif
from processingCTCFori import processingCTCFori
from assitingfunc import *
from generateInput import generate


if __name__ == '__main__':

    # ---- input settings ----
    celltype,chrom_lst=getSettings(sys.argv[1:])

    # ---- prepare ctcf motif ----
    orilst_lbm = extractMotif('lbm',chrId)
    orilst_known = extractMotif('known',chrId)
    orilst_disc = extractMotif('disc',chrId)

    try:
    # ---- process CTCF site decide with near cohesin ----
    # ---- and orientation decided according to motif ----
        final_ctcf_states = processingCTCFori(celltype,chrId,orilst_lbm,\
    										orilst_known, orilst_disc,bind_flxb,cap)

    # ---- output the list of ctcf sites ----
        writein_ctcf(celltype,chrId,cap,final_ctcf_states)

    # ---- generate the list of ctcf as input to the model ----
        generate(celltype,chrId,cap)

    except IOError:
        print('''
>>>> [WARNING]: Error in calculating CTCF-binding sites of %s!
                Please recheck the README file for detail.
'''%celltype)