#!/usr/bin/env python3

import os
from collections import Counter

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

sectors = []
for line in content.splitlines():
    code, checksum = line.split('[')  # ]
    checksum = checksum[:-1]

    code = code.split('-')
    letters = code[:-1]
    id = int(code[-1])

    letters = ''.join(letters)
    c = Counter(letters)
    cs = c.most_common()
    cs = sorted(cs, key=lambda x: (-x[1], x[0]))
    if checksum == ''.join(x[0] for x in cs[:5]):
        sectors.append(id)

    ltrs = ''
    for c in letters:
        ltrs += chr((ord(c) - 97 + id) % 26 + 97)
    if 'northpoleobjectstorage' == ltrs:
        print('Part 2:', id)


print('Part 1:', sum(sectors))
