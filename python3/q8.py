#!/usr/bin/env python3
import sys

DNAseq = sys.argv[1] #import in any argument given

DNAsequpper = DNAseq.upper()

RNA = DNAsequpper.replace('T','U')

print(RNA)