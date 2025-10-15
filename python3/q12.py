#!/usr/bin/env python3
import sys

DNAseq = sys.argv[1] #import in any argument given

DNAsequpper = DNAseq.upper() #Make it all upper case

sub_DNA = DNAsequpper[99:200]

A = sub_DNA.count('A')
T = sub_DNA.count('T')
C = sub_DNA.count('C')
G = sub_DNA.count('G')

GC = G + C
AT = A + T

totalDNA = len(sub_DNA)

print(f'The GC content is {GC/totalDNA:.0%}, and the AT content is {AT/totalDNA:.0%}.')
