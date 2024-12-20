#!/usr/bin/env python3

from functools import cache
import itertools
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

#content = '20\n15\n10\n5\n5'

containers = {}
for i, x in enumerate(content.splitlines()):
    containers[i] = int(x)

valid = set()

@cache
def find_containers(e, used = ()):
    if e == 0:
        valid.add(used)
        return 1

    count = 0
    found = False
    for c, v in containers.items():
        if v <= e and c not in used:
            new_used = list(used) + [c]
            new_used.sort()
            count += find_containers(e - v, tuple(new_used))
            found = True

    if not found:
        return 0

    return count

#find_containers(25)
find_containers(150)
print('Part 1:', len(valid))

min_length = min([len(x) for x in valid])
count = len([x for x in valid if len(x) == min_length])
print('Part 2:', count)
