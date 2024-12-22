#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

PRUNE = 16777216

def next_num(s):
    s2 = s * 64
    s = s ^ s2
    s = s % PRUNE

    s2 = s // 32
    s = s ^ s2
    s = s % PRUNE

    s2 = s * 2048
    s = s ^ s2
    s = s % PRUNE

    return s


def secret_number(num, count = 20):
    res = [num]
    s = num
    for i in range(count):
        s = next_num(s)
        res.append(s)

    return res


res = []
for line in content.splitlines():
    res.append(secret_number(int(line), 2000)[-1])

print('Part 1:', sum(res))

def ld(n):
    return int(str(n)[-1])

seq = {}
for line in content.splitlines():
    orig = int(line)
    n = int(line)
    c = []

    l = ld(n)
    c.append(l)

    for i in range(2000):
        n = next_num(n)
        l = ld(n)
        c.append(l)
        if len(c) > 5:
            c.pop(0)
        else:
            continue

        k = (c[1] - c[0], c[2] - c[1], c[3] - c[2], c[4] - c[3])
        if k not in seq:
            seq[k] = {}
        if orig in seq[k]:
            pass
        else:
            seq[k][orig] = l

values = []
for k, v in seq.items():
    values.append(sum(list(v.values())))
print('Part 2:', max(values))
