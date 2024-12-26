#!/usr/bin/env python3

import os
import re

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

possible = 0
cols = [
    [],
    [],
    []
]
for line in content.splitlines():
    nums = [int(x) for x in re.findall(r'\d+', line)]
    a, b, c = nums

    for i, n in enumerate(nums):
        cols[i].append(n)

    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        continue
    possible += 1

print('Part 1:', possible)

possible = 0
col = cols[0] + cols[1] + cols[2]
visited = []
for i in range(len(col)):
    if i in visited:
        continue

    visited.append(i)
    nums = [col[i]]
    for j in range(i+1, len(col)):
        visited.append(j)
        nums.append(col[j])
        if len(nums) == 3:
            break

    if len(nums) < 3:
        print(nums)
        continue

    a, b, c = nums
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        continue
    possible += 1

print('Part 2:', possible)
