#!/usr/bin/env python3

import os
import re

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

naughty = ['ab', 'cd', 'pq', 'xy']

score = 0
for line in content.splitlines():
    nope = False
    for n in naughty:
        if n in line:
            nope = True
            break

    if nope:
        continue

    twice = False
    for i in range(1, len(line)):
        if line[i-1] == line[i]:
            twice = True
            break

    if not twice:
        continue

    vowels = 0
    for c in line:
        if c in 'aeiuo':
            vowels += 1
        if vowels >= 3:
            break

    if vowels < 3:
        continue

    score += 1

print('Part 1:', score)

score = 0
for line in content.splitlines():
    twice = False
    for i in range(len(line)-1):
        chars = line[i:i+2]
        occ = [it.start() for it in re.finditer(chars, line)
               if (it.start() not in (i, i+1) and it.end() not in (i, i+1))]
        if len(occ):
            twice = True
            break
    if not twice:
        continue

    repeats = False
    for i in range(2, len(line)):
        if line[i-2] == line[i]:
            repeats = True
            break
    if not repeats:
        continue

    score += 1

print('Part 2:', score)
