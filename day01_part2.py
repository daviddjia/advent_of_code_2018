#!/usr/bin/env python

f = open('day01_input.txt','r')
freq = f.readlines()
f.close()
sum = 0
repeat_found = 0
past_freqs = set()
past_freqs.add(0)
while repeat_found == 0:
    for f in freq:
        f = f.strip()
        if f[0] == '+':
            sum += int(f[1:])
        else:
            sum -= int(f[1:])
        if sum in past_freqs:
            print sum
            repeat_found = 1
            break
        else:
            past_freqs.add(sum)
