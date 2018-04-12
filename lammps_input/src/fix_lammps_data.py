#!/usr/bin/env python

import sys
sys.path.append('/home/binz/Program/lmp_tools/lib/')
import lammps_tools as lmp
import fileinput

def assign_chromatin_state(csfile, hp):
    '''
    assign the states based on epigenetic marks
    '''
    hp.atom_types = []
    ncs = 20
    for ics in range(1,ncs+1):
        hp.add_atom_type(1.0, None, None)
    cs = []
    for line in fileinput.input(csfile):
        cs.append(int(line.split()[1]))
    
    for ia, atom in enumerate(hp.atoms):
        atom['atom_type_i'] = cs[ia]

if __name__ == "__main__":

    
    # fake ones
    coeffs = [30.0, 1.5, 1.0, 1.0]
    comment='fake'
    hp.add_bond_type(coeffs, comment)
    
    coeffs = [10.0, 30.0]
    hp.add_angle_type(coeffs, comment)
    
    hp.read_from_file('./build_initial_config/data.chromosome.angles')
    
    ## add two more angle types for ellipsoids
    #coeffs = [10.0, 30.0]
    #hp.add_angle_type(coeffs, comment)
    #coeffs = [10.0, 30.0]
    #hp.add_angle_type(coeffs, comment)
    
    #nAtom = len(hp.atoms)
    #for ia in range(1,nAtom-1):
        #atoml = (ia, ia+1, ia+1)
        #hp.add_angle(atoml, None, i=None, angle_type=hp.angle_types[1])

    #ia = nAtom-1
    #atoml = (ia, ia+1, ia+1)
    #hp.add_angle(atoml, None, i=None, angle_type=hp.angle_types[1])
    #hp.add_angle(atoml, None, i=None, angle_type=hp.angle_types[2])
    
    # fix box size
    #
    hp.box[0] = (-40, 40)
    hp.box[1] = (-40, 40)
    hp.box[2] = (-40, 40)
    
    # assign atom types
    # 
    csfile = './compartment_2tf/chr10_chromatin_states_From88000001To113000000_ctcf.txt'
    assign_chromatin_state(csfile)
    hp.write_to_file('./data.chromatin_states', ellipsoidFlag=0)

