#!/usr/bin/env python3

import os

from re import findall

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

ingr = {}
for line in content.splitlines():
    n = line.split(':')[0]
    c, d, v, t, cal = [int(x) for x in findall(r"-?\d+", line)]
    ingr[n] = (c, d, v, t, cal)

v = list(ingr.values())

def score(i, j, k, l, check_cals = False):
    if check_cals:
        cals = v[0][4] * i + v[1][4] * j + v[2][4] * k + v[3][4] * l
        if cals != 500:
            return 0

    c = v[0][0] * i + v[1][0] * j + v[2][0] * k + v[3][0] * l
    d = v[0][1] * i + v[1][1] * j + v[2][1] * k + v[3][1] * l
    f = v[0][2] * i + v[1][2] * j + v[2][2] * k + v[3][2] * l
    t = v[0][3] * i + v[1][3] * j + v[2][3] * k + v[3][3] * l

    if c <= 0 or d <= 0 or f <= 0 or t <= 0:
        return 0

    return c * d * f * t

full = 101
high_score = 0
high_score_500 = 0

for i in range(full):
    for j in range(full - i):
        for k in range(full - i - j):
            l = full - 1 - i - j - k
            s = score(i, j, k, l)
            high_score = max(high_score, s)
            s500 = score(i, j, k, l, True)
            high_score_500 = max(high_score_500, s500)

print('Part 1:', high_score)
print('Part 2:', high_score_500)
