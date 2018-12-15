#!/usr/bin/env python
from collections import deque
from adverplex.utilities import memoize

class Node(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    @memoize
    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        value = 0
        for i in self.metadata:
            if i-1 < len(self.children):
                value += self.children[i-1].value()
        return value

f = open('day08_input.txt','r')
lines = f.readlines()
f.close()

tree_list = []
for l in lines:
    tree_list.extend([int(num) for num in l.strip().split()])

root = Node()
stack = deque()
stack.append((tree_list[0], tree_list[1], root))
i = 2
while len(stack) != 0:
    # Pop header from stack
    if len(stack) != 0:
        header = stack.pop()

    # Store metadata
    if header[0] == 0:
        header[2].metadata = tree_list[i:i+header[1]]
        i += header[1]
        # Decrement child count on parent node
        if len(stack) != 0:
            prev_header = stack.pop()
            stack.append((prev_header[0]-1, prev_header[1], prev_header[2]))
    # Push child node onto stack
    else:
        child_node = Node()
        header[2].children.append(child_node)
        stack.append(header)
        stack.append((tree_list[i], tree_list[i+1], child_node))
        i += 2

# import ipdb. ipdb.set_trace()
print root.value()
