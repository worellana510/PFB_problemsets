#!/usr/bin/env python3
import sys

input("type book, song, tree, or organism")

thing = sys.argv[1] 
fav_things = {'book':'Greenlights','song':'Daddy Yankee - Gasolina','tree':'Purple Haze'}

if thing in fav_things:
    print(fav_things[thing])
