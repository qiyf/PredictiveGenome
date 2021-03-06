from Ipt_module import *
from Params import *
Params()

from assitingfunc import *

def processingCTCFori(celltype,chrId,orientation_list_lieberman, \
orientation_list_known, orientation_list_disc,bind_flxb,cap):
#
#	----	This function is to process the CTCF-binding sites with orientation	---- #
#	----	the output would be the atomic types with ctcf+ as 1, ctcf- as 2, other as 3, ctcf+- as 4	---- #
#

	in_path = '%s/raw.narrowPeak'%(glb_path)
	ctcf_peaks = np.loadtxt('%s/%s/ctcf/chip-seq_peak_%d.txt' \
							%(in_path,celltype,chrId))
	rad21_peaks = np.loadtxt('%s/%s/rad21/chip-seq_peak_%d.txt' \
							%(in_path,celltype,chrId))

	ctcf_states = []
	final_ctcf_states = []
	count_with_rad = 0		# count for the number of ctcf whose orientation has to be decided by cohesin
	count_no_rad = 0		# count for the number of ctcf who do not have near cohesin
	posSta = chr_region[chrId-1][1]*Mb

	for i in range(len(ctcf_peaks)):
		temp_pls_mns = []

		ctcfposSta = ctcf_peaks[i][0]
		ctcfposEnd = ctcf_peaks[i][1]
		ctcfposMid = 0.5*(ctcfposSta+ctcfposEnd)

		lo_motif = ctcfposSta-bind_flxb
		hi_motif = ctcfposEnd+bind_flxb

		radPos_min = process_minabs(ctcfposMid,rad21_peaks)

		for ori in range(len(orientation_list_lieberman)):
			ori_pos = int(orientation_list_lieberman[ori][0])
			if lo_motif <= ori_pos and hi_motif >= ori_pos:
				sign = orientation_list_lieberman[ori][1]
				temp_pls_mns.append(sign)
		
		if abs(radPos_min-ctcfposMid) <= cap:
			if ('+' in temp_pls_mns) and ('-' in temp_pls_mns):
				cs = 4
			elif ('+' in temp_pls_mns) and ('-' not in temp_pls_mns):
				cs = 1
			elif ('+' not in temp_pls_mns) and ('-' in temp_pls_mns):
				cs = 2
			else:
				if temp_pls_mns != []:
					print('> First check: sign vec is not empty, Error!')
					break
				for ori in range(len(orientation_list_known)):
					ori_pos = int(orientation_list_known[ori][0])
					if lo_motif <= ori_pos and hi_motif >= ori_pos:
						sign = orientation_list_known[ori][1]
						temp_pls_mns.append(sign)
				if ('+' in temp_pls_mns) and ('-' in temp_pls_mns):
					cs = 4
				elif ('+' in temp_pls_mns) and ('-' not in temp_pls_mns):
					cs = 1
				elif ('+' not in temp_pls_mns) and ('-' in temp_pls_mns):
					cs = 2
				else:
					if temp_pls_mns != []:
						print('> Second check: sign vec is not empty, Error!')
						break
					for ori in range(len(orientation_list_disc)):
						ori_pos = int(orientation_list_disc[ori][0])
						if lo_motif <= ori_pos and hi_motif >= ori_pos:
							sign = orientation_list_disc[ori][1]
							temp_pls_mns.append(sign)
					if ('+' in temp_pls_mns) and ('-' in temp_pls_mns):
						cs = 4
					elif ('+' in temp_pls_mns) and ('-' not in temp_pls_mns):
						cs = 1
					elif ('+' not in temp_pls_mns) and ('-' in temp_pls_mns):
						cs = 2
					else:
						count_with_rad += 1		# This is for ctcf that can have near cohesin
												# but no motif find
												# so has to decide the ori based on cohesin
						if ctcfposMid < radPos_min:
							cs = 1
						elif ctcfposMid > radPos_min:
							cs = 2
						else:
							cs = 0
			ctcf_states.append([ceil((ctcfposMid-posSta)/resolution),cs])
		else:
			count_no_rad += 1


	ctcf_tot = len(ctcf_peaks)
	rad21_rto = float(count_with_rad)/float(ctcf_tot)*100
	outer_rto = float(count_no_rad)/float(ctcf_tot)*100
	motif_rto = 100-outer_rto-rad21_rto

	ctcf_id = []
	ctcf_type = []
	for i in range(len(ctcf_states)):
		numid = ctcf_states[i][0]
		typeid = ctcf_states[i][1]
		if numid not in ctcf_id:
			ctcf_id.append(numid)
			ctcf_type.append(typeid)
		else:
			idx = ctcf_id.index(numid)
			ctcf_type[idx] = update_cs_type(ctcf_type[idx],typeid)
	if len(ctcf_id) != len(ctcf_type):
		print('> Double check error here.')

	for i in range(len(ctcf_type)):
		final_ctcf_states.append([ctcf_id[i],ctcf_type[i]])

	final_ctcf_states = np.array(final_ctcf_states)
	arg = np.argsort(final_ctcf_states[:,0])
	final_ctcf_states = final_ctcf_states[arg]	

	return final_ctcf_states
