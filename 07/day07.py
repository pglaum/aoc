#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

count = 0
ssl = 0
for line in content.splitlines():
    pairs = []
    brackets = []
    for i, c in enumerate(line):
        if c == '[':
            brackets.append([i])
        if c == ']':
            brackets[-1].append(i)

    i = 0
    in_brackets = False
    contains_in_brackets = False
    contains_abba = False
    while i < len(line):
        for b in brackets:
            if i == b[0]:
                in_brackets = True
                break
            if i == b[1]:
                in_brackets = False
                break
        if i < 3:
            i += 1
            continue

        c0, c1, c2, c3 = line[i-3:i+1]
        if c0 != c1 and c0 == c3 and c1 == c2:
            if in_brackets:
                contains_in_brackets = True
                break
            else:
                contains_abba = True
        i += 1

    if contains_abba and not contains_in_brackets:
        count += 1

    i = 0
    in_brackets = False
    hypernet = []
    abas = []
    while i < len(line):
        for b in brackets:
            if i == b[0]:
                in_brackets = True
                break
            if i == b[1]:
                in_brackets = False
                break
        if i < 2:
            i += 1
            continue

        c0, c1, c2 = line[i-2:i+1]
        if c0 != c1 and c0 == c2:
            if in_brackets:
                hypernet.append(line[i-2:i+1])
            else:
                abas.append(line[i-2:i+1])
        i += 1

    for aba in abas:
        search = f'{aba[1]}{aba[0]}{aba[1]}'
        if search in hypernet:
            ssl += 1
            break

print('Part 1:', count)
print('Part 2:', ssl)
