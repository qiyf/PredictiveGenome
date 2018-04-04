#!/usr/bin/env python

import sys
import os
from numpy import *

#   ----    chromatin state scripts     ----    #
sys.path.append('./lmps_data_scripts/')
sys.path.append('./simulation_scripts/')

from parse_chromhmm_files import *
from extract_neighboring_ctcf import *
from fix_lammps_data import *
from runOpt_3d import *

#
#   ----    chromosome setup    ------  #
def create_lmps_data(folder, chrId):

    #
    #   ----    create necessary folders    ----    #
    #

    lmps_folder = folder + '/lmps_data/'
    if os.path.exists(lmps_folder) is not True:
        os.mkdir(lmps_folder)

    chrom_state_folder = lmps_folder + '/chrom_states/'
    if os.path.exists(chrom_state_folder) is not True:
        os.mkdir(chrom_state_folder)

    ctcf_folder = lmps_folder + '/ctcfList'
    if os.path.exists(ctcf_folder) is not True:
        os.mkdir(ctcf_folder)

    #   
    #   ----    create chromatin state files    ----    #
    #

    csdir = '../chromatin_states/raw_data/OUTPUTSAMPLE_5kb_6celltype_15states/'

    infile = csdir + celltype+'_15_segments.bed'
    csfile = chrom_state_folder + 'chr%d_chromatin_states.txt'%chrId
    convert_to_5kb(infile, csfile, chrId)

    outfile = chrom_state_folder + \
    		'chr%d_chromatin_states_From%dTo%d.txt'%(chrId,gpos_sta, gpos_end)
    extract_chrom_state(csfile, outfile, chrId, resolution, gpos_sta, gpos_end)

    #   
    #   ----    extract neighboring ctcf    ----    #
    #

    ctcf_file = '../ctcf_sites/processingctcf/model_input/%s/ctcf_position_%s_chr%d_From%dMbTo%dMb.txt'\
    			%(celltype,celltype,chrId, chr_seg[chrId-1,1], chr_seg[chrId-1,2])
    extract_nearby_ctcf(ctcf_file, ctcf_folder)

    #   
    #   ----    create lammps data file    ----    #
    #

    create_data_file(lmps_folder,ctcf_file)


def create_data_file(lmps_folder,ctcf_file):

	hp = lmp.Data()
    coeffs = [30.0, 1.5, 1.0, 1.0]
    comment='nouse'
    hp.add_bond_type(coeffs, comment)
    
    coeffs = [10.0, 30.0]
    hp.add_angle_type(coeffs, comment)
    hp.read_from_file('./data_files/data.chromosome.init')
    
    # assign atom types
    assign_chromatin_state(ctcf_file, hp)
    hp.write_to_file(lmps_folder + '/data.chromatin_states', ellipsoidFlag=0)

def create_sim_folder(folder, chrId, iterId, nJobs, restartOpt=False):

    csfile = '../../lmps_data/chrom_states/chr%d_chromatin_states_From%dTo%d.txt'%(chrId, gpos_sta, gpos_end)
    pdbfile = './data_files/restart_file/chromosome10_centered.pdb'
    pbsfile =  '../../simulation_scripts/template.pbs'

    restartFolder = '/nobackup1/binz/chromosome_5kb/Gm12878/predict_all_chr_0.75/chr%d/iter%02d/'%(chrId, 134)

    lmpsTemplate = './simulation_scripts/lammps_template.in'
    paramsFolder = '../../../params/'

    for runId in range(nJobs):
        restartDCDFolder = restartFolder + 'run%02d/'%(runId)
        jobname='c%d_run%d'%(chrId, runId)
        prepare_simulation(folder, chrId, iterId, runId, jobname, csfile, restartDCDFolder, pdbfile, pbsfile, lmpsTemplate, paramsFolder)

def submit_jobs(folder, chrId, nJobs):

    workDir = os.getcwd()

    for runId in range(nJobs):
        rundir = folder + 'run%02d/'%runId
        cmd = "cd %s; sbatch job.pbs; cd %s"%(rundir, workDir)
        q = Popen(cmd, shell=True, stdout=PIPE)
        q.communicate()
    
def main(chrId, iterId):
    
    chrdir = globaldir + '/chr%d/'%chrId
    if os.path.exists(chrdir) is not True:
        os.mkdir(chrdir)

    simdir = chrdir + '/iter%02d/'%iterId
    if os.path.exists(simdir) is not True:
        os.mkdir(simdir)

    create_lmps_data(chrdir, chrId)

    nJobs = 4
    create_sim_folder(simdir, chrId, iterId, nJobs)
    submit_jobs(simdir, chrId, nJobs)

if __name__ == '__main__':

    celltype   = 'Gm12878'
    iterId = int(sys.argv[1])
    
    chr_seg = loadtxt('chr_region.txt')
    
    resolution = 5000
    Mb = 1000000

    for chrId in [2,3,4,5,6,7,8,9,13,14,15,16,20,22]:

        gpos_sta   = chr_seg[chrId-1,1]*Mb + 1
        gpos_end   = chr_seg[chrId-1,2]*Mb

        main(chrId, iterId)

