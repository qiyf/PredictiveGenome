# generate the VMD scripts

import fileinput as fi

def genVMDScript(celltype,chrId):
	
	# ---- generate the VMD script ---- #
	# ---- visualize the individual chromosome ---- #

	vmd_tmp = fi.input('./VMDScript/VMDColorTemplate.vmd')
	vmd = open('./VMDScript/VMDColor_%s_chr%d.vmd'%(celltype,chrId),'w')
	for line in vmd_tmp:
		if line[0:19] == 'mol new chr1_cs.pdb':
			vmd.write('mol new ../pdb/%s/chr%d_cs.pdb type pdb first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all\n'\
														%(celltype,chrId))
		elif line[0:23] == 'mol addfile chr1_cs.psf':
			vmd.write('mol addfile ../psf/%s/chr%d_cs.psf type psf first 0 last -1 step 1 filebonds 1 autobonds 1 waitfor all\n'\
														%(celltype,chrId))
		elif line[0:26] == 'mol rename top chr1_cs.psf':
			vmd.write('mol rename top ../psf/%s/chr%d_cs.psf\n'%(celltype,chrId))
		else:
			vmd.write(line)
	vmd.close()
	print('''   > VMD script for for %s, chromosome %d is generated.'''\
				%(celltype,chrId))

