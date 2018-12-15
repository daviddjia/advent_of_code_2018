#!/usr/bin/env python
import re

MAX_GEN = 20

f = open('day12_input.txt','r')
lines = f.readlines()
f.close()

regex = 'initial state: (.*)'
min_pot_num = -4
pot_gens = [re.search(regex, lines[0]).group(1).strip()]

rules = {}
for l in lines[2:]:
    rule = l.strip()
    regex = '(.*) => (.)'
    groups = re.search(regex, l)
    rules[groups.group(1)] = groups.group(2)

pot_zero_index = 0
for gen in range(MAX_GEN):
    pots = pot_gens[gen]
    buffered_pots = '....' + pots + '....'
    pot_zero_index -= 2
    next_gen_pots = ''
    for i in range(2, len(buffered_pots)-2):
        next_gen_pots += rules[buffered_pots[i-2:i+3]]
    while next_gen_pots[0] == '.':
        next_gen_pots = next_gen_pots[1:]
        pot_zero_index += 1
    while next_gen_pots[-1] == '.':
        next_gen_pots = next_gen_pots[:-1]
    pot_gens.append(next_gen_pots)
print pot_gens[MAX_GEN]

sum_pot_number = 0
for i in range(pot_zero_index, len(pot_gens[MAX_GEN])+pot_zero_index):
    if pot_gens[MAX_GEN][i-pot_zero_index] == '#':
        sum_pot_number += i
print sum_pot_number
