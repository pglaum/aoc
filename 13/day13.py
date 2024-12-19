#!/usr/bin/env python3

import os

from itertools import permutations

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

names = set()
values = {}
for line in content.splitlines():
    n1, _, dir, happiness, _, _, _, _, _, _, n2 = line[:-1].split(' ')
    happiness = int(happiness)
    if dir == 'lose':
        happiness = -happiness

    values[(n1, n2)] = happiness
    names.add(n1)
    names.add(n2)

def check_score(names):
    best = 0
    for p in permutations(names):
        score = 0
        for i in range(len(p)):
            n1 = p[i]
            n2 = p[i-1]
            score += values[(n1, n2)]
            score += values[(n2, n1)]

        best = max(score, best)

    return best

print('Part 1:', check_score(names))

for n in names:
    values[(n, 'me')] = 0
    values[('me', n)] = 0

names.add('me')
print('Part 2:', check_score(names))
