#!/usr/bin/env python

f = open('day01_input.txt','r')
freq = f.readlines()
f.close()
sum = 0
for f in freq:
    f = f.strip()
    if f[0] == '+':
        sum += int(f[1:])
    else:
        sum -= int(f[1:])
print sum
