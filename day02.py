#!/usr/bin/env python

f = open('day02_input.txt','r')
ids = f.readlines()
f.close()
twice_total = 0
thrice_total = 0
for i in ids:
    i = i.strip()
    twice = 0
    thrice = 0
    freq = {}
    for j in range(0, len(i)):
        if i[j] in freq:
            if freq[i[j]] == 1:
                twice += 1
            if freq[i[j]] == 2:
                twice -= 1
                thrice += 1
            if freq[i[j]] == 3:
                thrice -= 1
            freq[i[j]] += 1
        else:
            freq[i[j]] = 1
    twice_total += bool(twice)
    thrice_total += bool(thrice)
print twice_total * thrice_total
