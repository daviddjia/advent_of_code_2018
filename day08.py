#!/usr/bin/env python
from collections import deque

f = open('day08_input.txt','r')
lines = f.readlines()
f.close()

tree_list = []
for l in lines:
    tree_list.extend([int(num) for num in l.strip().split()])

metadata = []
stack = deque()
stack.append((tree_list[0], tree_list[1]))
i = 2
while len(stack) != 0:
    # Pop header from stack
    if len(stack) != 0:
        header = stack.pop()

    # Store metadata
    if header[0] == 0:
        metadata.extend(tree_list[i:i+header[1]])
        i += header[1]
        # Decrement child count on parent node
        if len(stack) != 0:
            prev_header = stack.pop()
            stack.append((prev_header[0]-1, prev_header[1]))
    # Push child node onto stack
    else:
        stack.append(header)
        stack.append((tree_list[i], tree_list[i+1]))
        i += 2

print sum(metadata)
