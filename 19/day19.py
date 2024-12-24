#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

mol = []
for line in content.split('\n\n')[0].splitlines():
    r1, r2 = line.split(' => ')
    mol.append((r1, r2))

word = content.split('\n\n')[1].strip()

def find_all(s, sub):
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

def repl_idx(s, i, l, sub):
    return s[:i] + sub + s[i+l:]

results = []
for m in mol:
    idx = find_all(word, m[0])
    for i in idx:
        results.append(repl_idx(word, i, len(m[0]), m[1]))

print('Part 1:', len(set(results)))

mol = sorted(mol, key=lambda m: -len(m[1]))

# greedy backtrack
def backtrack(word, steps = 0):
    if word == 'e':
        print('Part 2:', steps)
        exit(0)
        return [steps]

    results = []
    for k, v in mol:
        if v in word:
            results += backtrack(word.replace(v, k, 1), steps + 1)

    return results

backtrack(word, 0)
