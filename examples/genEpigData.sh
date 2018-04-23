#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
****** Getting start to generate chromatin states ******'''
cd $SHELL_FOLDER/../runMolecularDynamics/inputFiles/epig_input/chromStates/
python genChromState.py $1

echo '''
****** Getting start to generate CTCF-binding sites ******'''
cd $SHELL_FOLDER/../runMolecularDynamics/inputFiles/epig_input/ctcfSites/
python genCTCFbinding.py $1