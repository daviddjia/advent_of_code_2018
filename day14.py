#!/usr/bin/env python

max_recipes = 554401

recipes = [3, 7]
elf1 = 0
elf2 = 1

while len(recipes) < max_recipes+10:
    score_sum = recipes[elf1] + recipes[elf2]
    if score_sum >= 10:
        recipes.append(1)
        score_sum -= 10
    recipes.append(score_sum)
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

print recipes[-10:]
