#!/usr/bin/python

#
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : mpileup2phylip.py
#
#* Purpose : transform mpileup (with consensus base only, no counts !)
#  into phylip format sequence alignement
#
#   depends on biopython of course
#
#* Creation Date : 13-12-2014
#
#* Last Modified :
#
#* Created By : Etienne Loire
#
#  Usage: ./mpileup2phylip.py infile
#_._._._._._._._._._._._._._._._._._._._._.*/
#
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

#infile = open("test.mpileup",'r')
infile = open(sys.argv[1],'r')
first = infile.readline().split()
# Container for sample/population name
popname = first[1:]
# Container for sequences
seq = [""]*len(popname)
sec = infile.readline().split()

# name of scafforld, prsc / sc
prsc = sec[0]

# Concatenate sequences strings for this line
for i in range(len(sec[1:])):
    seq[i]+=sec[i+1]

for line in infile:
    c = line.split()
    sc= c[0]     # scaffold name for this line
    #  if new scaffold, write all data in file
    if sc!=prsc:
        handle = []
        for i in xrange(len(popname)):
            handle.append(SeqRecord(Seq(seq[i]),id = popname[i]))
        SeqIO.write(handle, open(prsc+".phylip",'w'), "phylip")
        # time to reinitialize sequences containers
        seq = [""]*len(popname)
        prsc=sc # update scaffold name
        # store data for this line in fresh container
        for i in range(len(c[1:])):
            seq[i]+=c[i+1]
    # add data for this line
    else:
        for i in range(len(c[1:])):
            seq[i]+=c[i+1]
        prsc=sc
# Don't forget last container !
handle = []
for i in xrange(len(popname)):
    handle.append(SeqRecord(Seq(seq[i]),id = popname[i]))

SeqIO.write(handle, open(sc+".phylip",'w'), "phylip")







