#!/usr/bin/env python
import re

MAX_GEN = 50000000000

f = open('day12_input.txt','r')
lines = f.readlines()
f.close()

regex = 'initial state: (.*)'
prev_gen_pots = re.search(regex, lines[0]).group(1).strip()

rules = {}
for l in lines[2:]:
    rule = l.strip()
    regex = '(.*) => (.)'
    groups = re.search(regex, l)
    rules[groups.group(1)] = groups.group(2)

pot_zero_index = 0
cyclic_pots = {prev_gen_pots: 0}
pots = ''
for gen in xrange(MAX_GEN):
    buffered_pots = '....' + prev_gen_pots + '....'
    pot_zero_index -= 2

    pots = ''
    for i in xrange(2, len(buffered_pots)-2):
        pots += rules[buffered_pots[i-2:i+3]]

    # Trimming pots list
    while pots[0] == '.':
        pots = pots[1:]
        pot_zero_index += 1
    while pots[-1] == '.':
        pots = pots[:-1]

    # Updated pot cycle tracker
    if pots not in cyclic_pots:
        cyclic_pots[pots] = pot_zero_index
    # Early out
    else:
        pot_zero_index += (pot_zero_index-cyclic_pots[pots])*(MAX_GEN-gen-1)
        break

    prev_gen_pots = pots

sum_pot_number = 0
for i in xrange(len(pots)):
    if pots[i] == '#':
        sum_pot_number += i+pot_zero_index
print pots
print sum_pot_number
