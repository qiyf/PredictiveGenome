from Ipt_module import *
from Params import *
Params()

def generate(celltype,chrId,cap):
# generate the input data format for the model
# common bead:3	ctcf+:1	ctcf-:2	ctcf+-:4

#	----	path to raw CTCF list
	to_path = '%s/processedCTCF/proc_data.%dbp/%s/'%(glb_path,cap,celltype)
	ctcf_path = '%s/ctcf_%d.txt'%(to_path,chrId)

#	----	path to input CTCF list
	gen_path = '%s/processedCTCF/model_input/%s/'%(glb_path,celltype)
	if not os.path.exists(gen_path):
        os.makedirs(gen_path)
    output_path = '%s/ctcf_position_%s_chr%d_From%dMbTo%dMb.txt'\
                %(gen_path,celltype,chrId,chr_region[chrId-1,1],chr_region[chrId-1,2])

#	----	processing
	tmp = np.loadtxt(ctcf_path)
	mat = np.zeros(nbead,2)
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

#	----	write to path for output
	fp = open(output_path,'w')
	for i in range(len(mat)):
		fp.writelines(str(mat[i][0]) + '\t' + str(mat[i][1]) + '\n')
	fp.close()