from Ipt_module import *

def generate(filename,output_path):
#
#	----	generate the input data format for the model
#	----	common bead:3	ctcf+:1	ctcf-:2	ctcf+-:4
#

	resolution = 5000					# resoltion for each bead
	Mb = 1E6
	nbeads = int(25*Mb/resoltion)
	tmp = np.loadtxt(filename)
	mat = np.zeros(nbeads,2)
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

	## write-in
	fp = open(output_path,'w')
	for i in range(len(mat)):
		fp.writelines(str(mat[i][0]) + '\t' + str(mat[i][1]) + '\n')
	fp.close()