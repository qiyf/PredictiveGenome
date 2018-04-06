# check running status
from Ipt_module import *
from Params import *
Params()

def check_status(usr_name,job_name):

	njob = -1
	while True:
		cmd = 'squeue |grep %s |grep %s |wc -l'%(usr_name,job_name)
		q = Popen(cmd, shell=True, stdout=PIPE)
		njob = int(q.communicate()[0])
		print (njob)
		if njob == 0:
			break
		else:
			time.sleep(10)