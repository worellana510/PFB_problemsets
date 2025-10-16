#!/usr/bin/env python3
import sys

fav_things = {'book':'Greenlights','song':'Daddy Yankee - Gasolina','tree':'Purple Haze','organism':'lion'}

#key = input(f'Choose your favorite key from {fav_things}: ')
#newvalue = input(f'Choose a new value for that key: ')

key = input(f'Choose your favorite key from {fav_things}: ')
if key in fav_things:
    newvalue = input (f'Choose a new value for that key: ')
    fav_things[key] = [newvalue]
    print(fav_things)
else: 
    print(f'Key not in dictionary!') 
print(f'value changed')


