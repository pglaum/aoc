#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

pos = (1, 1)
dirs = {
    'D': (1, 0),
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
}
keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

code = []
for line in content.splitlines():
    for c in line:
        prev_pos = pos
        pos = (pos[0] + dirs[c][0], pos[1] + dirs[c][1])

        if pos[0] < 0 or pos[0] > 2 or pos[1] < 0 or pos[1] > 2:
            pos = prev_pos

    code.append(keypad[pos[0]][pos[1]])

print('Part 1:', ''.join([str(x) for x in code]))

pos = (2,0)
keypad2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5,6,7,8,9],
    [None,'A','B','C',None],
    [None, None, 'D', None, None]
]

code = []
for line in content.splitlines():
    for c in line:
        prev_pos = pos
        pos = (pos[0] + dirs[c][0], pos[1] + dirs[c][1])

        if pos[0] < 0 or pos[0] > 4 or pos[1] < 0 or pos[1] > 4 or keypad2[pos[0]][pos[1]] == None:
            pos = prev_pos

    code.append(keypad2[pos[0]][pos[1]])

print('Part 2:', ''.join([str(x) for x in code]))
