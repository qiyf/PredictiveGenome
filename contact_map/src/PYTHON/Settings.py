

class Settings():

	global celltype,runnum,chrom_lst,clus_bool,job_name,ptn_name
	
#	---- default: calculate Gm12878 chromosome 1 with 8 parallel simulations
	celltype = 'Gm12878'
	runnum = 8
	chrom_lst = [1]

#	---- default: calculate on clusters
	clus_bool = True

#	---- default: the job and partition name if calculate on cluster
	job_name = 'cmap'
	ptn_name = 'sched_mit'
	