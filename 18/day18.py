#!/usr/bin/env python3

import copy
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

lights = [list(line) for line in content.splitlines()]

dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

for _ in range(100):
    next_lights = copy.deepcopy(lights)

    for i in range(len(lights)):
        for j in range(len(lights[i])):
            nc = 0
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if ni < 0 or nj < 0 or ni >= len(lights) or nj >= len(lights[i]):
                    continue
                if lights[ni][nj] == '#':
                    nc += 1

            #print((i, j), nc)
            if lights[i][j] == '#':
                if nc in [2, 3]:
                    next_lights[i][j] = '#'
                else:
                    next_lights[i][j] = '.'
            else:
                if nc == 3:
                    next_lights[i][j] = '#'
                else:
                    next_lights[i][j] = '.'

    lights = copy.deepcopy(next_lights)

res = sum([x.count('#') for x in lights])
print('Part 1:', res)

lights = [list(line) for line in content.splitlines()]
lights[0][0] = '#'
lights[0][len(lights)-1] = '#'
lights[len(lights)-1][0] = '#'
lights[len(lights)-1][len(lights)-1] = '#'

for _ in range(100):
    next_lights = copy.deepcopy(lights)
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            nc = 0
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if ni < 0 or nj < 0 or ni >= len(lights) or nj >= len(lights[i]):
                    continue
                if lights[ni][nj] == '#':
                    nc += 1

            #print((i, j), nc)
            if lights[i][j] == '#':
                if nc in [2, 3]:
                    next_lights[i][j] = '#'
                else:
                    next_lights[i][j] = '.'
            else:
                if nc == 3:
                    next_lights[i][j] = '#'
                else:
                    next_lights[i][j] = '.'

    next_lights[0][0] = '#'
    next_lights[0][len(lights)-1] = '#'
    next_lights[len(lights)-1][0] = '#'
    next_lights[len(lights)-1][len(lights)-1] = '#'
    lights = copy.deepcopy(next_lights)

res = sum([x.count('#') for x in lights])
print('Part 2:', res)
