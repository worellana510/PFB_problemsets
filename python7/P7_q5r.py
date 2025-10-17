#!/usr/bin/env python3
import re

fastaDict={}
with open('Python_07.fasta.txt','r') as dna_obj:
    for line in dna_obj:
        line = line.rstrip()
        header = re.search(r"^>.*",line)
        if header:
            seqname = header.group()
            fastaDict[seqname] = ''
        else:
            fastaDict[seqname] = fastaDict[seqname] + line
        print(fastaDict)







