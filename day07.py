#!/usr/bin/env python
import re
import heapq

class Step(object):
    def __init__(self, name, prereqs):
        self.name = name
        self.prereqs = prereqs
    def __str__(self):
        return "(%s, %s)" % (len(self.prereqs), self.name)
    def __eq__(self, other):
        return (len(self.prereqs),self.name)==(len(other.prereqs),other.name)
    def __cmp__(self, other):
        return cmp(
            (len(self.prereqs),self.name),
            (len(other.prereqs),other.name),
        )

f = open('day07_input.txt','r')
lines = f.readlines()
f.close()

steps = {}
rules = {}
for l in lines:
    regex = 'Step (.) must be finished before step (.) can begin'
    groups = re.search(regex, l)
    step_name = groups.group(2)
    prereq_name = groups.group(1)

    if step_name not in steps:
        steps[step_name] = Step(step_name, set(prereq_name))
    else:
        steps[step_name].prereqs.add(prereq_name)
    if prereq_name not in steps:
        steps[prereq_name] = Step(prereq_name, set())

    if prereq_name not in rules:
        rules[prereq_name] = [step_name]
    else:
        rules[prereq_name].append(step_name)
for prereq_name in rules:
    rules[prereq_name] = [steps[step_name] for step_name in rules[prereq_name]]

ordered_steps = steps.values()
heapq.heapify(ordered_steps)

order = ''
while len(ordered_steps) > 0:
    step = heapq.heappop(ordered_steps)
    order += step.name
    if step.name in rules:
        for blocked_step in rules[step.name]:
            blocked_step.prereqs.remove(step.name)
        heapq.heapify(ordered_steps) # To account for side effects

print order
