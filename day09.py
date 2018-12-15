#!/usr/bin/env python
import re

f = open('day09_input.txt','r')
lines = f.readlines()
f.close()

regex = '(\d*) players; last marble is worth (\d*) points'
groups = re.search(regex, lines[0])
num_players = int(groups.group(1))
last_marble = int(groups.group(2))

current_player = 0
circle = [0]
current_marble_index = 0
players = [0 for i in xrange(num_players)]
for marble in xrange(1, last_marble+1):
    if marble % 23 != 0:
        current_marble_index = (current_marble_index + 2) % len(circle)
        if current_marble_index == 0:
            current_marble_index = len(circle)
        circle.insert(current_marble_index, marble)
    else:
        players[current_player] += marble
        current_marble_index = (current_marble_index-7) % len(circle)
        players[current_player] += circle.pop(current_marble_index)
        if current_marble_index == len(circle):
            current_marble_index = 0
    current_player = (current_player + 1) % num_players

print max(players)
