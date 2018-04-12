#!/usr/bin/env python

#  quies    1
# fairew    2
#    low    3
#   pol2    4
#  gen3'    5
#   elon    6
#   ctcf    7
#   enhw    8
#  enhwf    9
#  elonw   10
#  promf   11
#   tssf   12
#    tss   13
#  h4k20   14
# dnaseu   15
#  gen5'   16
#  reprw   17
#   repr   18
#  ctcfo   19
# dnased   20
#  reprd   21
#    art   22
#  promp   23
#   enhf   24
#    enh   25

from numpy import *
import fileinput

def extract_chrom_state(infile, outfile, chrId,res, csta, cend, realPos=False):

    chrom = 'chr%d'%chrId

    fo = open(outfile, 'w')
    for line in fileinput.input(infile):
        items = line.split()
        gpos = int(items[0])

        if gpos >=csta and gpos <= cend:

            if realPos:
                fo.write('%8d %4d\n'%(gpos, int(items[1][1::])))
            else:
                fo.write('%8d %4d\n'%((gpos-csta)/res+1, int(items[1][1::])))

    fo.close()

def extract_chrom_state_7celltypes(mapfile, infile, outfile, chrId,res, csta, cend, realPos=False):

    map_7to6 = {}
    for line in fileinput.input(mapfile):
        if line[0] == '#':
            continue
        else:
            items = line.split()
            map_7to6[items[0]] = int(items[1])

    chrom = 'chr%d'%chrId

    fo = open(outfile, 'w')
    for line in fileinput.input(infile):
        items = line.split()
        gpos = int(items[0])

        if gpos >=csta and gpos <= cend:

            if realPos:
                #fo.write('%8d %4d\n'%(gpos, int(items[1][1::])))
                fo.write('%8d %4d\n'%(gpos, map_7to6[items[1][1::]] ))
            else:
                #fo.write('%8d %4d\n'%((gpos-csta)/res+1, int(items[1][1::])))
                fo.write('%8d %4d\n'%((gpos-csta)/res+1, map_7to6[items[1][1::]] ))

    fo.close()


def convert_to_5kb(infile, outfile, chrId):

    chrom = 'chr%d'%chrId

    fo = open(outfile, 'w')
    for line in fileinput.input(infile):
        items = line.split()
        if items[0] == chrom:
            gsta = int(items[1])
            gend = int(items[2])

            for gp in range(gsta, gend, 5000):
                fo.write('%d %s\n'%(gp, items[3]))
    fo.close()


if __name__=='__main__':
    celltype = 'Gm12878'
    chrId = 10

    res = 5000
    csta =  88000001
    cend = 113000000
    csdir = '/nobackup1/binz/chromosome_5kb/OUTPUTSAMPLE_ucsc_5kb_6celltype_15states/'

    infile = csdir + celltype+'_15_segments.bed'
    csfile = 'chr%d_chromatin_states.txt'%chrId
    convert_to_5kb(infile, csfile, chrId)

    outfile = 'chr%d_chromatin_states_From%dTo%d.txt'%(chrId,csta,cend)
    extract(csfile, outfile, chrId, res, csta, cend)

    # ctcf
    csdir = '/nobackup1/binz/chromosome_5kb/OUTPUTSAMPLE_ucsc_5kb_transcript_5celltypes2marks_4states/'

    infile = csdir + celltype+'_4_segments.bed'
    csfile = 'chr%d_ctcf.txt'%chrId
    convert_to_5kb(infile, csfile, chrId)

    realPos = True
    outfile = 'chr%d_ctcf_From%dTo%d.txt'%(chrId,csta,cend)
    extract(csfile, outfile, chrId, res, csta, cend, realPos)
