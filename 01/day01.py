#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

ops = content.strip().split(', ')

pos = (0, 0)
cdir = 0
dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

visited = [pos]
HQ = None
for op in ops:
    if op[0] == 'R':
        cdir += 1
    else:
        cdir -= 1
    cdir %= 4

    l = int(op[1:])
    for i in range(l):
        pos = (pos[0] + dirs[cdir][0], pos[1] + dirs[cdir][1])

        if pos in visited and not HQ:
            print('HQ:', pos)
            HQ = pos
        visited.append(pos)


print('Part 1:', abs(pos[0]) + abs(pos[1]))
print('Part 2:', abs(HQ[0]) + abs(HQ[1]), HQ)
