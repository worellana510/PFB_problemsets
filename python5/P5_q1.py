#!/usr/bin/env python3
import sys

thing = sys.argv[1] 
fav_things = {'book':'Greenlights','song':'Daddy Yankee - Gasolina','tree':'Purple Haze'}

if thing in fav_things:
    print(fav_things[thing])

#book = fav_things['book']
#print(book)
#print(fav_things['tree'])
#print(fav_things['tree'])

# fav_things['organism'] = "dog" # adding a new key and value to an existing dictionary.

# length = len(fav_things)
# print(length)

# print(fav_things['organism'])

# for thing in fav_things:
#     fav = fav_things[thing]
#     print(thing,fav)