#!/bin/bash

git clone -b stable https://github.com/lammps/lammps.git lammps

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)

cp $SHELL_FOLDER/src/lammps/Makefile.openmpi $SHELL_FOLDER/lammps/src/MAKE/
cp $SHELL_FOLDER/src/lammps/force.cpp $SHELL_FOLDER/lammps/src/
ln -s $SHELL_FOLDER/src/lammps/pair_tanhlr_cut_ideal.cpp $SHELL_FOLDER/lammps/src/pair_tanhlr_cut_ideal.cpp
ln -s $SHELL_FOLDER/src/lammps/pair_tanhlr_cut_ideal.h $SHELL_FOLDER/lammps/src/pair_tanhlr_cut_ideal.h
ln -s $SHELL_FOLDER/src/lammps/pair_tanhlr_cut_ideala.cpp $SHELL_FOLDER/lammps/src/pair_tanhlr_cut_ideala.cpp
ln -s $SHELL_FOLDER/src/lammps/pair_tanhlr_cut_ideala.h $SHELL_FOLDER/lammps/src/pair_tanhlr_cut_ideala.h

echo '''
>>>> Connected with the LAMMPS src files.'''
echo '''
>>>> Starting to compile LAMMPS ......
'''
cd $SHELL_FOLDER/lammps/src/
make clean-all
make yes-molecule
make yes-class2
make -j 4 openmpi
