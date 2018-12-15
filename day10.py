#!/usr/bin/env python
from __future__ import print_function
import re
import sys
import time
import copy

f = open('day10_input.txt','r')
lines = f.readlines()
f.close()

points = {}
min_x = sys.maxint
max_x = -sys.maxint-1
min_y = sys.maxint
max_y = -sys.maxint-1
for l in lines:
    regex = 'position=<\s*(-?\d*),\s*(-?\d*)>\s*velocity=<\s*(-?\d*),\s*(-?\d*)>'
    groups = re.search(regex, l)
    x_position = int(groups.group(1))
    y_position = int(groups.group(2))
    x_velocity = int(groups.group(3))
    y_velocity = int(groups.group(4))
    position = (x_position, y_position)
    velocity = (x_velocity, y_velocity)
    if position not in points:
        points[position] = set([velocity])
    else:
        points[position].add(velocity)
    if x_position > max_x:
        max_x = x_position
    if x_position < min_x:
        min_x = x_position
    if y_position > max_y:
        max_y = y_position
    if y_position < min_y:
        min_y = y_position

def print_sky(my_points):
    sorted_points = sorted(my_points.keys())
    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x+1):
            char = '.'
            if (i, j) in my_points:
                char = '#'
            print(char, end='')
        print()
    print()

# print_sky(points)

prev_y_range = sys.maxint
iter_count = 0
old_points = {}
while max_y-min_y<prev_y_range:
    new_min_x = sys.maxint
    new_max_x = -sys.maxint-1
    new_min_y = sys.maxint
    new_max_y = -sys.maxint-1
    new_points = {}
    for point in points.keys():
        velocities = points[point]
        for velocity in velocities:
            moved_point = (point[0]+velocity[0], point[1]+velocity[1])
            if moved_point not in new_points:
                new_points[moved_point] = set([velocity])
            else:
                new_points[moved_point].add(velocity)

            if moved_point[0] > new_max_x:
                new_max_x = moved_point[0]
            if moved_point[0] < new_min_x:
                new_min_x = moved_point[0]
            if moved_point[1] > new_max_y:
                new_max_y = moved_point[1]
            if moved_point[1] < new_min_y:
                new_min_y = moved_point[1]

    del old_points # forcing some garbage collection
    old_points = points
    points = new_points

    prev_y_range = max_y-min_y
    min_x = new_min_x
    max_x = new_max_x
    min_y = new_min_y
    max_y = new_max_y

    # time.sleep(1)
    # print_sky(points)

    iter_count += 1
    print('Iteration %s' % iter_count)

print_sky(old_points)
