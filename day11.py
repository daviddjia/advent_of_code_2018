#!/usr/bin/env python
import sys

serial_number = 7139
grid = [[0 for i in xrange(300)] for j in xrange(300)]

for i in xrange(300):
    for j in xrange(300):
        grid[j][i] = ((i+10)*j+serial_number)*(i+10)/100%10-5

max_power = -sys.maxint-1
max_power_coord = (-1, -1)
for i in xrange(300-2):
    for j in xrange(300-2):
        power = 0
        for x in xrange(i, i+3):
            for y in xrange(j, j+3):
                power += grid[y][x]
        if power > max_power:
            max_power = power
            max_power_coord = (i, j)
print max_power
print "(%s,%s)" % (max_power_coord[0], max_power_coord[1])
