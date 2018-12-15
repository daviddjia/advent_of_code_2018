#!/usr/bin/env python
import re

class Node(object):
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

def add_marble(current_marble, value):
    current_marble = current_marble.next_node
    new_marble = Node(
        value=value,
        prev_node=current_marble,
        next_node=current_marble.next_node)
    current_marble.next_node.prev_node = new_marble
    current_marble.next_node = new_marble
    return new_marble

def remove_marble(current_marble):
    for i in xrange(7):
        current_marble = current_marble.prev_node
    current_marble.prev_node.next_node = current_marble.next_node
    current_marble.next_node.prev_node = current_marble.prev_node
    return (current_marble.next_node, current_marble.value)

f = open('day09_input.txt','r')
lines = f.readlines()
f.close()

regex = '(\d*) players; last marble is worth (\d*) points'
groups = re.search(regex, lines[0])
num_players = int(groups.group(1))
last_marble_value = int(groups.group(2))*100

current_player = 0
current_marble = Node(value=0, prev_node=None, next_node=None)
current_marble.prev_node = current_marble
current_marble.next_node = current_marble
players = [0 for i in xrange(num_players)]
for value in xrange(1, last_marble_value+1):
    if value % 23 != 0:
        current_marble = add_marble(current_marble, value)
    else:
        players[current_player] += value
        (current_marble, removed_marble_value) = remove_marble(current_marble)
        players[current_player] += removed_marble_value
    current_player = (current_player + 1) % num_players

print max(players)
