#!/usr/bin/env python
from numpy import * 
from subprocess import *
import os
import fileinput
import mdtraj as md

same_mol_flag_ideal = 0
same_mol_flag_tanh  = 1

def prepare_simulation(globaldir, chrId, iterId, runId, jobname, csfile, restartDCDFolder, pdbfile, pbsfile, lmpsTemplate, paramsFolder):

    rundir = globaldir + "/run%02d/"%(runId)
    if ( os.path.exists(rundir) is not True ):
        os.makedirs(rundir)
    workDir = os.getcwd()

    traj = md.load('%s/DUMP_FILE.dcd'%restartDCDFolder, top=pdbfile)
    #traj = md.load('%s/DUMP_FILE_highT.dcd'%restartDCDFolder, top=pdbfile)
    nf = len(traj)

    # create pbs file
    pbsFile = rundir + "job.pbs"
    pbs_tmp = fileinput.input(pbsfile)
    pf = open(pbsFile, 'w')
    # header
    head = '''#!/bin/bash

#SBATCH --job-name=%s
''' %(jobname)
    pf.write(head)
    # tmp
    for line in pbs_tmp:
        pf.write(line)
    pf.close()

    # lammps input file with custom random seed
    inFile = rundir + "in.chromosome"
    in_tmp = fileinput.input(lmpsTemplate)
    pf = open(inFile, 'w')
    pf.write('variable        rseed equal   %d\n'%(4928459+runId) )
    for line in in_tmp:
        if line[0:9] == 'read_dump':
            pf.write('read_dump       %s/DUMP_FILE.dcd %d x y z  format molfile dcd /home/binz/Program/lib/vmd.old/plugins/LINUXAMD64/molfile\n'%(restartDCDFolder, nf-1))
        elif line[0:10] == 'pair_style':
            pf.write('pair_style      hybrid/overlay table linear 10000 tanhlr/cut/ideala 6.0 %d 15 %s/ideal_chromosome_iter%02d.txt %s tanhlr/cut/ideal 6.0 %s/ideal_chromosome_tad_iter%02d.txt ../../lmps_data/ctcfList/ctcfInd.txt 0.75 4\n'%(same_mol_flag_ideal, paramsFolder, iterId, csfile, paramsFolder, iterId))
        elif line[0:20] == 'include         XXXX':
            pass
        else:
            pf.write(line)

    pf.close()

if __name__ == '__main__':

    iterId = 1;
    
    for runId in range(20):
        runJob(iterId, runId)

