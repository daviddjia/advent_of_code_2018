#!/usr/bin/env python

pattern = '554401'

recipes = ['3', '7']
elf1 = 0
elf2 = 1

while True:
    score_sum = int(recipes[elf1]) + int(recipes[elf2])
    if score_sum >= 10:
        recipes.append('1')
        score_sum -= 10
    recipes.append(str(score_sum))
    elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
    elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)

    if len(recipes) >= len(pattern):
        if pattern == ''.join(recipes[-len(pattern):]):
            print len(recipes)-len(pattern)
            break
    if len(recipes) >= len(pattern)+1:
        if pattern == ''.join(recipes[-len(pattern)-1:-1]):
            print len(recipes)-len(pattern)-1
            break
