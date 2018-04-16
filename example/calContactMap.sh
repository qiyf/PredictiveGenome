#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
>>>> Getting start to calculate the contact map ......
'''
cd $SHELL_FOLDER/../contactMap/
python calContactMap.py $1 $2 $3 $4