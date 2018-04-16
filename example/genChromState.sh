#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
>>>> Getting start to generate chromatin states ......
'''
cd $SHELL_FOLDER/../chromatinStates/
python genChromState.py