#!/usr/bin/env python3

import os
import numpy as np

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

goal = int(content)

BIG = 1000000

houses_a = np.zeros(BIG)
houses_b = np.zeros(BIG)

for elf in range(1, BIG):
    houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1) * 50:elf] += 11 * elf

print('Part 1:', np.nonzero(houses_a >= goal)[0][0])
print('Part 2:', np.nonzero(houses_b >= goal)[0][0])
