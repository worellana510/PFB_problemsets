#!/usr/bin/env python3

import re #When using regular expressions in python you have to import in the program

#nobody_obj = open("Python_07_nobody.txt","r") #This opens the file into an object
#nobody = nobody_obj.read() #this reads the file similiar to cat and puts into a vairable. 

#print(nobody) #Now I can print the file on the interpreter.

#found = re.findall(r"Nobody", nobody)
#print(found)
#print(len(found))

#question 1: Find the position of the word nobody.  
# with open("Python_07_nobody.txt","r") as nobody:
#     for line in nobody:
#         for match in re.finditer(r"Nobody",line):
#             print(match.start())

#question 2: Replace nobody with Shayla
# with open("Python_07_nobody.txt","r") as nobody:
#     for line in nobody:
#         newsong = re.sub(r"Nobody","Shayla",line)
#         print(newsong)

#question 3: 
# with open('Python_07.fasta.txt','r') as dna_obj:
#     for line in dna_obj:
#         line = line.rstrip()
#         found = re.search(r"^>",line)
#         print(found)

#question 4:
# with open('Python_07.fasta.txt','r') as dna_obj:
#     for (id, desc) in re.findall(r"^>\b(\w+\b)", dna_obj):
#         print("id:",id)


