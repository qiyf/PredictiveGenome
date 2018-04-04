import sys
sys.path.append('./src/')

from Ipt_module import *
from processingMotif import extract_motif_orientation
from processingCTCFori import extract_ctcf_states_orientations
from assitingfunc import *
from generateInput import generate


if __name__ == '__main__':

    #
    # ---- input settings ----
    #	
    chr_region = np.loadtxt('../chr_region.txt')
    if len(sys.argv) == 1: celltype='Gm12878'; chrId=1; bind_flxb=100; cap=50
    elif len(sys.argv) == 3: celltype=sys.argv[1]; chrId=int(sys.argv[2]); bind_flxb=100; cap=50
    else: celltype=sys.argv[1]; chrId=int(sys.argv[2]); bind_flxb=int(sys.argv[3]); cap=int(sys.argv[4])	# 'bind_flxb' is motif matching +/- buffer, default is 100bp
    																										# 'cap' is nearest cohesin requirement, default is 50bp

    #
    # ---- prepare ctcf motif ----
    #																									
    motif_fi_lbm	= './motif_file/motif_lbm/motif_chr%d.txt'%chrId
    motif_fi_known 	= './motif_file/motif_known/motif_chr%d.txt'%chrId
    motif_file_disc	= './motif_file/motif_disc/motif_chr%d.txt'%chrId
    orientation_list_lbm = extract_motif_orientation(motif_fi_lbm)
    orientation_list_known = extract_motif_orientation(motif_fi_known)
    orientation_list_disc = extract_motif_orientation(motif_file_disc)

    try:
    #
    # ---- process CTCF site decide with near cohesin ----
    # ---- and orientation decided according to motif ----
    #
        in_path = './raw.narrowPeak'
        ctcf_peaks = np.loadtxt('%s/%s/ctcf/chip-seq_peak_%d.txt'%(in_path,celltype,chrId))
        rad21_peaks = np.loadtxt('%s/%s/rad21/chip-seq_peak_%d.txt'%(in_path,celltype,chrId))
        final_ctcf_states = extract_ctcf_states_orientations(ctcf_peaks,rad21_peaks,orientation_list_lbm,\
    											orientation_list_known, orientation_list_disc,bind_flxb,cap)

    #
    # ---- output the list of ctcf sites ----
    #		
        to_path = './processedCTCF/proc_data.%dbp/%s/'%(cap,celltype)
        if not os.path.exists(to_path):
            os.makedirs(to_path)
        fo = open('%s/ctcf_%d.txt'%(to_path,chrId),'w')
        np.savetxt(fo,final_ctcf_states,fmt='%d')
        fo.close()

    #
    # ---- generate the list of ctcf as input to the model ----
    #
        gen_path = './processedCTCF/model_input/%s/'%(celltype)
        if not os.path.exists(gen_path):
            os.makedirs(gen_path)
        output_path = '%s/ctcf_position_%s_chr%d_From%dMbTo%dMb.txt'\
                                    %(gen_path,celltype,chrId,chr_region[chrId-1,1],chr_region[chrId-1,2])
        generate('%s/ctcf_%d.txt'%(to_path,chrId),output_path)

    except IOError:
        print('\n[WARNING]: Please recheck the README about the available cell types....\n')
