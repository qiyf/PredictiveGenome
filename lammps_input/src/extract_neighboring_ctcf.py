#!/usr/bin/env python

import fileinput
from numpy import *

def extractCtcfConv(infile, out_folder):

    ctcfL = []
    ctcfR = []
    natom = 0
    for line in fileinput.input(infile):
        natom += 1
        items = line.split()
        aid = int(items[0])
        ct  = int(items[1])
        if (ct == 1):
            ctcfL.append(aid)
        elif (ct == 2):
            ctcfR.append(aid)
        elif (ct == 4):
            ctcfL.append(aid)
            ctcfR.append(aid)
        else:
            pass

    fileinput.close()

    savetxt(out_folder + '/ctcfL.txt', array(ctcfL), fmt='%d')
    savetxt(out_folder + '/ctcfR.txt', array(ctcfR), fmt='%d')

    ctcfInd = zeros((natom,2), dtype='int')
    ctcfList = zeros((natom,2), dtype='int')
    for aid in range(1, natom+1):

        tmp = -1
        for cid in ctcfL:
            if cid <= aid:
                if cid > tmp:
                    tmp = cid
            else:
                break

        if tmp == -1:
            ctcfInd[aid-1,0] = tmp
            ctcfList[aid-1,0] = tmp
        else:
            ctcfInd[aid-1,0] = ctcfL.index(tmp)
            ctcfList[aid-1,0] = tmp

        tmp = natom+1
        for cid in ctcfR:
            if cid >= aid:
                if cid < tmp:
                    tmp = cid

        if tmp <= natom:
            ctcfInd[aid-1,1] = ctcfR.index(tmp)
            ctcfList[aid-1,1] = tmp
        else:
            ctcfInd[aid-1,1] = -1
            ctcfList[aid-1,1] = -1

    savetxt(out_folder + '/ctcfList.txt', ctcfList, fmt='%d')
    savetxt(out_folder + '/ctcfInd.txt', ctcfInd, fmt='%d')

def extractCtcfnonConv(infile, out_folder):

    ctcf = []
    natom = 0
    for line in fileinput.input(infile):
        natom += 1
        items = line.split()
        aid = int(items[0])
        ct  = int(items[1])
        if (ct == 1):
            ctcf.append(aid)
        elif (ct == 2):
            ctcf.append(aid)
        elif (ct == 4):
            ctcf.append(aid)
        else:
            pass

    fileinput.close()

    ctcfList = zeros((natom,2), dtype='int')
    for aid in range(1, natom+1):

        tmp = -1
        for cid in ctcf:
            if cid <= aid:
                if cid > tmp:
                    tmp = cid
            else:
                break

        if tmp == -1:
            ctcfList[aid-1,0] = tmp
        else:
            ctcfList[aid-1,0] = ctcf.index(tmp)
            #ctcfList[aid-1,0] = tmp

        tmp = natom+1
        for cid in ctcf:
            if cid >= aid:
                if cid < tmp:
                    tmp = cid

        if tmp <= natom:
            ctcfList[aid-1,1] = ctcf.index(tmp)
            #ctcfList[aid-1,1] = tmp
        else:
            ctcfList[aid-1,1] = -1

    savetxt(out_folder + '/ctcfList.txt', ctcfList, fmt='%d')

if __name__ == "__main__":
    infile = '../compartment_2tf/ctcf_position_chr21_Hela_20MBto45MB_5kb.txt'

    extract_nearby_ctcf(infile, './')

