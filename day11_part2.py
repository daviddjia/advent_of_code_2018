#!/usr/bin/env python
import sys

serial_number = 7139
grid = [[0 for i in xrange(300)] for j in xrange(300)]

max_power = -sys.maxint-1
max_power_coord = (-1, -1, -1)
memoized_power = {}
for i in xrange(300):
    for j in xrange(300):
        power = ((i+10)*j+serial_number)*(i+10)/100%10-5
        grid[j][i] = power
        memoized_power[i, j, 1] = power
        if power > max_power:
            max_power = power
            max_power_coord = (i, j, 1)

for size in xrange(2, 301):
    for i in xrange(300-size+1):
        for j in xrange(300-size+1):
            power = memoized_power[i, j, size-1]
            power += sum(grid[j+size-1][i:i+size])
            for y in xrange(j, j+size-1):
                power += grid[y][i+size-1]
            memoized_power[i, j, size] = power
            if power > max_power:
                max_power = power
                max_power_coord = (i, j, size)
print max_power
print "(%s,%s,%s)" % (max_power_coord[0],max_power_coord[1],max_power_coord[2])
