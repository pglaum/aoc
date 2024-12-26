#!/usr/bin/env python3

import os
import numpy as np
import re
from pprint import pprint

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

screen = np.zeros((6, 50), dtype=bool)

for line in content.splitlines():
    if line.startswith('rect'):
        x, y = [int(z) for z in re.findall(r'\d+', line)]
        screen[0:y,0:x] = True
    elif 'row' in line:
        row, rot = [int(z) for z in re.findall(r'\d+', line)]
        screen[row] = np.concatenate([screen[row,-rot:], screen[row,:-rot]])
    elif 'column' in line:
        col, rot = [int(z) for z in re.findall(r'\d+', line)]
        screen[:,col] = np.concatenate([screen[-rot:,col], screen[:-rot,col]])

for l in screen:
    line = ''
    for c in l:
        if c:
            line += '#'
        else:
            line += '.'
    print(line)
print()

print('Part 1:', np.count_nonzero(screen))
