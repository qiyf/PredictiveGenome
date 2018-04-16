#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
>>>> Getting start to run simulation ......
'''
cd $SHELL_FOLDER/../runSimulation/
python main.py $1 $2 $3 $4 $5 $6