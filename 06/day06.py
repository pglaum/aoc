#!/usr/bin/env python3

from collections import Counter
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

cols = {}
for line in content.splitlines():
    for i, c in enumerate(line):
        if i not in cols:
            cols[i] = []
        cols[i].append(c)

mc = ''
lc = ''
for col in cols.values():
    c = Counter(col)
    common = c.most_common()
    mc += common[0][0]
    lc += common[-1][0]

print('Part 1:', mc)
print('Part 2:', lc)
