from Ipt_module import *

class Params():

	global Mb,resolution,nbead,glb_path,chr_region
	
#	---- default: 25Mb segment, at resolution of 5kb
	Mb=1E6
	resolution=5000
	nbead=int(25*Mb/resolution)

#	---- default: global path
	_cmd = 'pwd'
	q = Popen(_cmd, shell=True, stdout=PIPE)
	path_tpl = q.communicate()
	glb_path = path_tpl[0].split('\n')[0]

#	---- chromosome segment region
	chr_region = np.loadtxt('%s/../chr_region.txt'%glb_path)
