#!/usr/bin/env python3
import sys

number = int(sys.argv[1]) #argument given to it by the command line.


if number > 0: 
    #print("Is positive")
    if number < 50:
        print("Its positive and less than 50")
    elif number == 50:
        print("Number is 50")
    else: 
        print("Its positive and greater than 50")
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
   

#elif number < 0:
#print("Is negative")
# #elif number < 50:
#     print(number, "Is less than 50")
# #elif number > 50:
#     print(number, "Is larger than 50")
# #elif number/3:
#     print(number,"Is divisible by 3")
# elif number == 0:
#     print(number,"Is equal to 0")
# else:
#     print(number,"Is special")