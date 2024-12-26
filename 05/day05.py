#!/usr/bin/env python3

import os
from hashlib import md5

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read().strip()

salt = 1
password = ''
chars = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]

while None in chars:
    h = ''
    while not h.startswith('00000'):
        h = md5(f'{content}{salt}'.encode()).hexdigest()
        salt += 1

    print('char:', h, '->', h[5])
    password += h[5]
    if h[5].isnumeric() and int(h[5]) < 8 and not chars[int(h[5])]:
        chars[int(h[5])] = h[6]
        print(h[5], '->', h[6])
    print()

print('Part 1:', password)
print('Part 2:', ''.join(chars))
