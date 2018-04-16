#!/bin/bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
echo '''
>>>> Getting start to generate CTCF-binding sites ......
'''
cd $SHELL_FOLDER/../ctcfBindingSites/
python genCTCFbinding.py