#!/usr/bin/env python3

petty_obj = open("Python_06.txt","r")
contents = petty_obj.read()
contents = contents.upper()

upperPetty = open("Python_06_uc.txt","w")
upperPetty.write(contents)

upperPetty.close()

print(upperPetty)
