#!/usr/bin/env python3

#dnaseq_obj = open('python6test.txt','r')
# dna= dnaseq_obj.read()


#dna = 'ATGCTCGTT'

with open('Python_06.seq.txt','r') as dnaseq_obj: #open('revpython6test.txt','w') as dnaseq_write:
    for line in dnaseq_obj:
        line = line.rstrip()
        list = line.split('\t')
        sequence = list[1]
        sequencename = list[0]
        sequence = sequence.replace('A','1')
        sequence = sequence.replace('T','2')
        sequence = sequence.replace('C','3')
        sequence = sequence.replace('G','4')
        sequence = sequence.replace('1','T')
        sequence = sequence.replace('2','A')
        sequence = sequence.replace('3','G')
        sequence = sequence.replace('4','C')
        rev = sequence[::-1] #This allowed me to reverse the complement.
        list[1] = rev
        print(f'{list[0]}\t{list[1]}')







