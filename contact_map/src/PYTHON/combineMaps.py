# combine to generate ensemble average contact map
from Ipt_module import *
from Params import *
Params()

def combine_cmaps(celltype,chromid,iterid,runnum):
	nf_tot = 0
	comb_map = np.zeros([nbead_cg,nbead_cg])

	cmap_path = './%s/chr%d/iter%03d/run%02d/'\
				%(celltype,chromid,iterid,runid)

	if os.path.exists('%s/contact_map_CG.txt'%cmap_path):
		for run_id in range(0,runnum):
			in_temp = np.loadtxt('%s/contact_map_CG.txt'%cmap_path)
			nf = np.loadtxt('%s/nframes.txt'%cmap_path)

			comb_map += in_temp*nf
			nf_tot += nf

		comb_map /= nf_tot
		np.savetxt('./cmap/contact_map_CG_comb_chr%d_iter%d.txt'\
					%(chromid,iterid),comb_map,fmt = '%.8f')
		print('contact_map_CG_%d is combined sucessfully!'%chromid)
	
	else:
		print('Error in combining the contact maps of chromosome %d!'%chromid)