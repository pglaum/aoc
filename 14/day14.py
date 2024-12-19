#!/usr/bin/env python3

import os

from collections import Counter
from itertools import accumulate, cycle

fdir = os.path.dirname(os.path.realpath(__file__))
length = 2503

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

reindeers = {}
for line in content.splitlines():
    n, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = line.split()
    reindeers[n] = (int(speed), int(time), int(rest))

distance = 0
for name, v in reindeers.items():
    speed, time, rest = v
    base = length // (time + rest)
    bmod = length % (time + rest)

    d = base * time * speed

    if bmod >= time:
        d += time * speed
    else:
        d += bmod * speed

    distance = max(distance, d)

print('Part 1:', distance)

points = 0
history = {}
for n, v in reindeers.items():
    speed, time, rest = v
    steps = cycle([speed] * time + [0] * rest)
    history[n] = list(accumulate(next(steps) for _ in range(2503)))

points = [
    i
    for a in zip(*history.values())
    for i, v in enumerate(a) if v == max(a)
]
by_points = max(Counter(points).values())

print('Part 2:', by_points)
