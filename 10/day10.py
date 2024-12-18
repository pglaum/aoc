#!/usr/bin/env python3

import os

from itertools import groupby

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read().strip()

def look_and_say(input):
    return ''.join(str(len(list(g))) + k for k, g in groupby(input))

say = content
score40 = 0
for i in range(50):
    say = look_and_say(say)

    if i == 39:
        print('Part 1:', len(say))

print('Part 2:', len(say))
