#!/usr/bin/env python

f = open('day02_input.txt','r')
ids = f.readlines()
f.close()
twice_total = 0
thrice_total = 0
substr_set = set()
for i in ids:
    i = i.strip()
    for j in range(0, len(i)):
        substr = (j, i[0:j] + i[j+1:len(i)])
        if substr in substr_set:
            print substr
        else:
            substr_set.add(substr)
