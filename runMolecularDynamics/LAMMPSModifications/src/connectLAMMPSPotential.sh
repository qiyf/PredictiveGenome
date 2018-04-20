#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
>>>> Connected with the LAMMPS potential files.
'''

cp $SHELL_FOLDER/Makefile.openmpi $SHELL_FOLDER/../../../lammps/src/MAKE/
ln -s ../../PredictiveGenome/lammpsCode/src/pair_tanhlr_cut_ideal.cpp $SHELL_FOLDER/../../../lammps/src/pair_tanhlr_cut_ideal.cpp
ln -s ../../PredictiveGenome/lammpsCode/src/pair_tanhlr_cut_ideal.h $SHELL_FOLDER/../../../lammps/src/pair_tanhlr_cut_ideal.h
ln -s ../../PredictiveGenome/lammpsCode/src/pair_tanhlr_cut_ideala.cpp $SHELL_FOLDER/../../../lammps/src/pair_tanhlr_cut_ideala.cpp
ln -s ../../PredictiveGenome/lammpsCode/src/pair_tanhlr_cut_ideala.h $SHELL_FOLDER/../../../lammps/src/pair_tanhlr_cut_ideala.h
