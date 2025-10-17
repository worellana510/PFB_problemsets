#!/usr/bin/env python3

fastaDict={}
with open('Python_07.fasta.txt','r') as dna_obj:
    for line in dna_obj:
        line = line.rstrip()
        if line.startswith('>'):
            seqID = line.replace('>','')
            fastaDict[seqID] = ''
        else:
            seq = line 
            fastaDict[seqID] = fastaDict[seqID] + seq
    print(fastaDict)
        







