#!/usr/bin/env python

f = open('day03_input.txt','r')
lines = f.readlines()
f.close()

FABRIC_WIDTH = 1000
FABRIC_LENGTH = 1000

fabric = [[0 for i in range(FABRIC_WIDTH)] for j in range(FABRIC_LENGTH)]
potential_areas = [0 for i in range(len(lines))]

for l in lines:
    l = l.strip().split()
    num = int(l[0][1:])
    coordinates = l[2][:-1].split(',')
    x = int(coordinates[0])
    y = int(coordinates[1])
    dimensions = l[3].split('x')
    width = int(dimensions[0])
    length = int(dimensions[1])
    potential_areas[num-1] = width*length

    for i in range(x, x+width):
        for j in range(y, y+length):
            if fabric[i][j] != 0:
                fabric[i][j] = 'x'
            else:
                fabric[i][j] = num

actual_areas = [0 for i in range(len(lines))]
for i in range(FABRIC_WIDTH):
    for j in range(FABRIC_LENGTH):
        if fabric[i][j] != 'x' and fabric[i][j] != 0:
            actual_areas[fabric[i][j]-1] += 1

for i, actual_area in enumerate(actual_areas):
    if actual_area == potential_areas[i]:
        print i+1
