#!/usr/bin/env python3
import re

# ApoI_obj = open('Python_07_ApoI.fasta.txt','r')
# ApoI = ApoI_obj.read()
# print(ApoI)

with open('Python_07_ApoI.fasta.txt','r') as Apo_obj:
    for line in Apo_obj:
        line = line.strip()
        for match in re.findall(r"[AG]AATT[CT]",line):
            print(match)


