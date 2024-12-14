#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

pos = (0, 0)
dirs = {
    '>': (0, 1),
    '^': (1, 0),
    '<': (0, -1),
    'v': (-1, 0),
}
houses = [pos]

for i, c in enumerate(content):
    pos = (pos[0] + dirs[c][0], pos[1] + dirs[c][1])
    houses.append(pos)

print('Part 1:', len(set(houses)))

pos = (0, 0)
rpos = (0, 0)
houses = [pos]
robot = False

for i, c in enumerate(content):
    if robot:
        rpos = (rpos[0] + dirs[c][0], rpos[1] + dirs[c][1])
        houses.append(rpos)
    else:
        pos = (pos[0] + dirs[c][0], pos[1] + dirs[c][1])
        houses.append(pos)

    robot = not robot

print('Part 2:', len(set(houses)))