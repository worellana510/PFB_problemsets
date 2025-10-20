#!/usr/bin/env python3

import sys

#question 6: 

def reversecomplement(dna):
    dna = dna[::-1] #reversed the sequence.
    dna = dna.upper() #makes it upper just in case input is mixed between upper and lower. 
    dna = dna.replace('A','1')
    dna = dna.replace('T','2')
    dna = dna.replace('G','3')
    dna = dna.replace('C','4') 
    dna = dna.replace('1','T')
    dna = dna.replace('2','A')
    dna = dna.replace('3','C')
    dna = dna.replace('4','G') #this will give the complement strand.
    return dna

print(reversecomplement('GCTGTGATATTGA'))


