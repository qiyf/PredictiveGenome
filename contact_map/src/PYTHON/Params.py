

class Params():

	global cg_fac,num_kb,nbead_cg,startb,endb,startfr
	
#	---- default: visulize the map at 50kb
	cg_fac = 10
	num_kb = 5*cg_fac
	nbead_cg = int(5000/cg_fac*0.8)

#	---- default: calculate the 20Mb (2Mb-22Mb) out of total 25Mb
	startb = 400
	endb = 4400

#	---- default: start calculation from the 1st frame	
	startfr = 1
	
