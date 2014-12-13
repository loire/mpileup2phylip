#!/usr/bin/python

#
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : mpileup2phylip.py
#
#* Purpose :
#
#* Creation Date : 13-12-2014
#
#* Last Modified :
#
#* Created By :
#
#_._._._._._._._._._._._._._._._._._._._._.*/
#
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

infile = open("test.mpileup",'r')
first = infile.readline().split()
popname = first[1:]
seq = [""]*len(popname)
sec = infile.readline().split()
prsc = sec[0]
for i in range(len(sec[1:])):
    seq[i]+=sec[i+1]

for line in infile:
    c = line.split()
    sc= c[0]
    if sc!=prsc:
        handle = []
        for i in xrange(len(popname)):
            handle.append(SeqRecord(Seq(seq[i]),id = popname[i]))
        SeqIO.write(handle, open(prsc+".phylip",'w'), "phylip")
        seq = [""]*len(popname)
        prsc=sc
        for i in range(len(c[1:])):
            seq[i]+=c[i+1]
    else:
        for i in range(len(c[1:])):
            seq[i]+=c[i+1]
        prsc=sc

handle = []
for i in xrange(len(popname)):
    handle.append(SeqRecord(Seq(seq[i]),id = popname[i]))

SeqIO.write(handle, open(sc+".phylip",'w'), "phylip")







