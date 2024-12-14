#!/usr/bin/env python3

with open('input', 'r') as f:
    content = f.read()

floor = 0
for i, c in enumerate(content):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

    if floor == -1:
        print('Part 2', i + 1)

print('Part 1:', floor)