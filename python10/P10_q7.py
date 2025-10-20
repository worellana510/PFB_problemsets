#!/usr/bin/env python3

import subprocess

#question 7: 

output = subprocess.run(['ls','-l'], stdout=subprocess.PIPE)
bytes = output.stdout
stdout = bytes.decode('utf-8)')

lines = stdout.splitlines()
lenlines = len(lines)

print(lines[0])
print(lines[7])
print(lenlines)





