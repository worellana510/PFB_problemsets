#!/usr/bin/env python3

#Question 1: Create a class that contains a sequence, its name, and its
#organims of origin. 

class DNAsequence(object):
    def __init__(self, sequence, gene_name, organism_name):
        self.sequence = sequence.upper()
        self.gene_name = gene_name
        self.organism_name = organism_name
    
    def dnalength(self):
        length = len(self.sequence)
        return length
    
    def ntcompo(self):
        uppercase = self.sequence
        nt_count = {}
        for nt in uppercase:
            if nt in nt_count:
                nt_count[nt] += 1
            else:
                nt_count[nt] = 1
        return nt_count
    
    def GCcontent(self):
        seq = self.sequence
        if len(seq) == 0:
            return 0.0
        gc = seq.count('G') + seq.count('C')
        return (gc / len(seq))
    
    def fastaformatter(self):
        fasta = f'>{self.gene_name} {self.organism_name} \n {self.sequence}'
        return fasta

# dnaobj1 = DNAsequence('ATGCCTGTACCGTACGT', 'CIDEB', 'Homo sapiens')
# dnaobj2 = DNAsequence('ATGCCGATAGCGTGCGTA', 'CYM', 'Mus musculus')

# for d in [dnaobj1, dnaobj2]:
#     print('name:', d.gene_name,'\n', 'seq:',d.sequence,'\n','organism:', d.organism_name)

dnarecord = DNAsequence('ATGCGATCTGAATT', 'FoxA1', 'Mus musculus')

print(f'The length of the dna strand is {dnarecord.dnalength()}.')    
print(f'The DNA composition of the sequence is {dnarecord.ntcompo()}.')
print(f'The GC content of the sequence is {dnarecord.GCcontent():.2%}.')
print(f'My fasta format is the following:{dnarecord.fastaformatter()}')