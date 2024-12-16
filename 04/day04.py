#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()
content = content.strip()

import hashlib

i = 1
while True:
    m = hashlib.md5(f"{content}{i}".encode())
    if m.hexdigest().startswith('00000'):
        print('Part 1:', i)

    if m.hexdigest().startswith('000000'):
        print('Part 2:', i)
        break

    i += 1
