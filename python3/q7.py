#!/usr/bin/env python3
import sys

DNAtoRNA = sys.argv[1] #import in any argument given

RNA = DNAtoRNA.replace('T','U')

print(RNA)

