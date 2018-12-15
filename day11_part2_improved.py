#!/usr/bin/env python
import sys
import copy

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

x_grid = copy.deepcopy(grid)
y_grid = copy.deepcopy(grid)
for i in xrange(300):
    for j in xrange(300):
        if i > 0:
            x_grid[j][i] += x_grid[j][i-1]
        if j > 0:
            y_grid[j][i] += y_grid[j-1][i]

for size in xrange(2, 301):
    for i in xrange(300-size+1):
        for j in xrange(300-size+1):
            power = memoized_power[i, j, size-1]
            if i > 0:
                power += x_grid[j+size-1][i+size-1] - x_grid[j+size-1][i-1]
            else:
                power += x_grid[j+size-1][i+size-1]
            if j > 0:
                power += y_grid[j+size-2][i+size-1] - y_grid[j-1][i+size-1]
            else:
                power += y_grid[j+size-2][i+size-1]
            memoized_power[i, j, size] = power
            if power > max_power:
                max_power = power
                max_power_coord = (i, j, size)
print max_power
print "(%s,%s,%s)" % (max_power_coord[0],max_power_coord[1],max_power_coord[2])
