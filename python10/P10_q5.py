#!/usr/bin/env python3

import sys

#question 5: 

def percentGC(dna):

    dna = dna.upper()

    A = dna.count('A')
    T = dna.count('T')
    C = dna.count('C')
    G = dna.count('G')

    GC = G + C
    AT = A + T

    totalDNA = len(dna)
    return print(f'The GC content is {GC/totalDNA:.0%}, and the AT content is {AT/totalDNA:.0%}.')

percentGC('CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA')