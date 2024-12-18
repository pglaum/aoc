#!/usr/bin/env python3

import os
import re

import numpy as np

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

lights = np.zeros((1000, 1000), dtype=bool)

for l in content.splitlines():
    i1, j1, i2, j2 = [int(x) for x in re.findall(r'\d+', l)]
    what = -1
    if l.startswith('turn on'):
        what = 1
    elif l.startswith('turn off'):
        what = 0

    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            match what:
                case 1:
                    lights[(i, j)] = True
                case 0:
                    lights[(i, j)] = False
                case -1:
                    lights[(i, j)] = not lights[(i, j)]

count = 0
for i in range(1000):
    for j in range(1000):
        if lights[(i, j)]:
            count += 1
print('Part 1:', count)

#
# part 2
#

lights = np.zeros((1000, 1000), dtype=int)

for l in content.splitlines():
    i1, j1, i2, j2 = [int(x) for x in re.findall(r'\d+', l)]
    what = 2
    if l.startswith('turn on'):
        what = 1
    elif l.startswith('turn off'):
        what = -1

    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
            if what < 0 and lights[(i, j)] > 0:
                lights[(i, j)] -= 1
            if what > 0:
                lights[(i, j)] += what

count = 0
for i in range(1000):
    for j in range(1000):
        count += lights[(i, j)]
print('Part 2:', count)
