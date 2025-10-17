#!/usr/bin/env python3

fastaDict={}
with open('fasta2.txt','r') as dna_obj:
    for line in dna_obj:
        line = line.rstrip()
        if line.startswith('>'):
            seqID = line.replace('>','')
            fastaDict[seqID] = ''
        else:
            seq = line 
            fastaDict[seqID] = fastaDict[seqID] + seq




        # columns = line.split('\n')
        # key, values = columns[0], columns[1:]
        # fastaDict[key] = values


print(fastaDict)
#print(fastaDict['>seq1'])

        







