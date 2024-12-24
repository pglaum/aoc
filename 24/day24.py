#!/usr/bin/env python3

from functools import reduce
from itertools import combinations
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

pkgs = [int(x) for x in content.splitlines()]
qe = lambda g: reduce(int.__mul__, g, 1)

def can_be_split(items, target, n):
    for l in range(1, len(items) - n + 1):
        for c in (g for g in combinations(items, l) if sum(g) == target):
            if n == 2 and sum(items - set(c)) == target:
                return True
            elif can_be_split(items - set(c), target, n - 1):
                return True

def solve(items, n):
    hitstarget = lambda g: sum(g) == target
    isvalidsplit = lambda g: can_be_split(set(items) - set(g), target, n-1)
    target = sum(items) // n
    for l in range(1, len(items)):
        c = combinations(items, l)
        g = sorted(filter(hitstarget, c), key=qe)
        for result in g:
            if isvalidsplit(result):
                return qe(result)
    return None

print('Part 1:', solve(pkgs, 3))
print('Part 2:', solve(pkgs, 4))
