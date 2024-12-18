#!/usr/bin/env python3

import os
import sys

from itertools import permutations

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

places = set()
distances = {}
for line in content.splitlines():
    n1, _, n2, _, dist = line.split(' ')
    dist = int(dist)
    places.add(n1)
    places.add(n2)

    distances.setdefault(n1, {})[n2] = int(dist)
    distances.setdefault(n2, {})[n1] = int(dist)

short = sys.maxsize
long = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    short = min(short, dist)
    long = max(long, dist)

print('Part 1:', short)
print('Part 2:', long)
