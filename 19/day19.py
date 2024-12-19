#!/usr/bin/env python3

from functools import cache
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

patterns = content.splitlines()[0].split(', ')
designs = content.splitlines()[2:]


@cache
def try_towel(t):
    count = 0
    for p in patterns:
        if t == p:
            count += 1
        if t.startswith(p):
            count += try_towel(t[len(p):])

    return count

count = 0
arrs = 0
for i, t in enumerate(designs):
    c = try_towel(t)
    if c > 0:
        count += 1
    arrs += c

print('Part 1:', count)
print('Part 2:', arrs)
