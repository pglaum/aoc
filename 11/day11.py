#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

def check_requirement(p):
    good = False
    ords = [ord(c) for c in p]
    for i in range(2, len(ords)):
        if ords[i] - ords[i-2] == 2 and ords[i] - ords[i-1] == 1:
            good = True
    if not good:
        return 1

    if 'i' in p or 'o' in p or 'l' in p:
        return 2

    pairs = 0
    paired = []
    for i in range(1, len(p)):
        if p[i-1] == p[i] and i not in paired and (i - 1) not in paired:
            paired += [i, i-1]
            pairs += 1
    if pairs < 2:
        return 3

    return 0

def next_password(p):
    for i in range(1, len(p) + 1):
        end_after = False
        nc = ''
        if p[-i] == 'z':
            nc = 'a'
        else:
            nc = chr(ord(p[-i]) + 1)
            end_after = True

        if i > 1:
            p = p[:-i] + nc + p[-i + 1:]
        else:
            p = p[:-1] + nc

        if end_after:
            break

    return p

pw = content.strip()
while check_requirement(pw) != 0:
    pw = next_password(pw)
print('Part 1:', pw)

pw = next_password(pw)
while check_requirement(pw) != 0:
    pw = next_password(pw)
print('Part 2:', pw)
