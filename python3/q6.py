#!/usr/bin/env python3
import sys

DNAseq = sys.argv[1] #import in any argument given

DNAsequpper = DNAseq.upper()

A = DNAsequpper.count('A')
T = DNAsequpper.count('T')
C = DNAsequpper.count('C')
G = DNAsequpper.count('G')

print(f'There are {A} A nucleotides, {T} T nucleotides, {C} C nucleotides and {G} G nucleotides in this DNA sequence')

