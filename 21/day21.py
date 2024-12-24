#!/usr/bin/env python3

import os
import re
from math import ceil

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

boss = []
for l in content.splitlines():
    boss.append(int(re.findall(r'\d+', l)[0]))

weapons = {
    'd': (8, 4, 0),
    's': (10, 5, 0),
    'w': (25, 6, 0),
    'l': (40, 7, 0),
    'g': (74, 8, 0),
}

armor = {
    ' ': (0, 0, 0),
    'l': (13, 0, 1),
    'c': (31, 0, 2),
    's': (53, 0, 3),
    'b': (75, 0, 4),
    'p': (102, 0, 5),
}

rings = {
    ' ': (0, 0, 0),
    '  ': (0, 0, 0),
    'a1': (25, 1, 0),
    'a2': (50, 2, 0),
    'a3': (100, 3, 0),
    'd1': (20, 0, 1),
    'd2': (40, 0, 2),
    'd3': (80, 0, 3),
}

def simulate(you, boss):
    boss_hits = ceil(boss[0] / max(you[1] - boss[2], 1))
    your_hits = ceil(you[0] / max(boss[1] - you[2], 1))

    if boss_hits <= your_hits:
        return True

    return False


def stats(w, a, r1, r2):
    return [100, w[1] + r1[1] + r2[1], a[2] + r1[2] + r2[2]]

lowest = 100000
highest = 0
none = [0, 0, 0]
for w in weapons.values():
    for a in armor.values():
        for k1, r1 in rings.items():
            for k2, r2 in rings.items():
                if k1 == k2:
                    continue
                cost = w[0] + a[0] + r1[0] + r2[0]
                if simulate(stats(w, a, r1, r2), boss):
                    if cost < lowest:
                        lowest = cost
                else:
                    highest = max(highest, cost)

print('Part 1:', lowest)
print('Part 2:', highest)
