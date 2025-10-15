#!/usr/bin/env python3
import sys

DNAseq = sys.argv[1] #import in any argument given

A = DNAseq.count('A')
T = DNAseq.count('T')
C = DNAseq.count('C')
G = DNAseq.count('G')

GC = G + C
AT = A + T

totalDNA = len(DNAseq)

print(f'The GC content is {GC/totalDNA:.0%}, and the AT content is {AT/totalDNA:.0%}.')

