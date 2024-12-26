#!/usr/bin/env python3

import os
import re

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

row, col = [int(x) for x in re.findall(r'\d+', content)]

FIRST = 20151125
MUL = 252533
DIV = 33554393

nums = [FIRST]


def get_idx(row, col):
    r_start = 1
    for i in range(1, row):
        r_start += i
    for i in range(1, col):
        r_start += (row + i)

    return r_start

idx = get_idx(row, col)
num = FIRST
for i in range(idx-1):
    num = (num * MUL) % DIV

print('Part 1:', num)
