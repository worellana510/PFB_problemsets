#!/usr/bin/env python3

petty_obj = open("Python_06.txt","r")
contents = petty_obj.read()
contents = contents.upper()
#for line in contents.split("\n"):
#   line = line.rstrip()
#   print(line)
print(contents)
petty_obj.close()


