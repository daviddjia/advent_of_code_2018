#!/usr/bin/env python
from __future__ import print_function
import re
import sys

class Ground(object):

    spring_x_pos = 500

    def __init__(self, raw_ground_input):
        self.x_max = self.y_max = 0
        self.x_min = self.y_min = sys.maxint
        processed_ground_input = []
        for l in raw_ground_input:
            x_start = x_end = y_start = y_end = -1
            regex = '(.)=(\d*), .=(\d*)..(\d*)'
            groups = re.search(regex, l)
            coord = groups.group(1)
            if coord=='x':
                x_start = x_end = int(groups.group(2))
                y_start = int(groups.group(3))
                y_end = int(groups.group(4))
            elif coord == 'y':
                y_start = y_end = int(groups.group(2))
                x_start = int(groups.group(3))
                x_end = int(groups.group(4))
            else:
                print("Error!")
            if x_start < self.x_min:
                self.x_min = x_start
            if x_end > self.x_max:
                self.x_max = x_end
            if y_start < self.y_min:
                self.y_min = y_start
            if y_end > self.y_max:
                self.y_max = y_end
            processed_ground_input.append((x_start, x_end, y_start, y_end))

        self.grid = [
            # Extra columns on either side to account for water spillage
            ['.' for i in xrange(self.x_min-1, self.x_max+2)]
            # Extra row on top in case water falls right onto clay on first row
            for j in xrange(self.y_min-1, self.y_max+1)
        ]
        self.x_offset = self.x_min-1
        self.y_offset = self.y_min-1
        for (x_start, x_end, y_start, y_end) in processed_ground_input:
            for x_pos in xrange(x_start-self.x_offset, x_end+1-self.x_offset):
                for y_pos in xrange(y_start-self.y_offset, y_end+1-self.y_offset):
                    self.grid[y_pos][x_pos] = '#'

    def print_ground(self):
        for y in xrange(len(self.grid)):
            # Extra columns on either side to account for water spillage
            for x in xrange(len(self.grid[0])):
                print(self.grid[y][x], end='') 
            print('')
        print('')
 
    def stream(self, x, y, direction):
        if self.grid[y][x] == '.':
            self.grid[y][x] = '|'

        spread_out = False
        if y+1 == len(self.grid) or self.grid[y+1][x] == '|':
            return False
        elif self.grid[y+1][x] == '.':
            spread_out = self.stream(x, y+1, 0)
        else:
            spread_out = True

        if spread_out:
            settled = True
            if direction <= 0 and self.grid[y][x-1] != '#':
                settled = self.stream(x-1, y, -1) and settled
                if x-1 == 0: # Hit edge
                    settled = False
            if direction >= 0 and self.grid[y][x+1] != '#':
                settled = self.stream(x+1, y, 1) and settled
                if x+1 == len(self.grid[0])-1: # Hit edge
                    settled = False
            if direction == 0 and settled:
                i = x
                while self.grid[y][i] != '#':
                    self.grid[y][i] = '~'
                    i += 1
                i = x-1
                while self.grid[y][i] != '#':
                    self.grid[y][i] = '~'
                    i -= 1
            return settled
        return False

    def run(self):
        self.grid[0][self.spring_x_pos-self.x_offset] = '+'
        self.stream(self.spring_x_pos-self.x_offset, 1, 0)

    def count_water(self):
        count = 0
        # Discount extra row and two extra columns
        for y in xrange(1, len(self.grid)):
            for x in xrange(len(self.grid[0])):
                if self.grid[y][x] in ('|', '~'):
                    count += 1
        return count

def main():
    f = open('day17_input.txt','r')
    lines = f.readlines()
    f.close()
    ground = Ground(raw_ground_input=lines)
    # ground.print_ground()
    sys.setrecursionlimit(2500) # Dangerous hack!!
    ground.run()
    ground.print_ground()
    print("Total amount of water: %s" % ground.count_water())

if __name__ == "__main__":
    main()
