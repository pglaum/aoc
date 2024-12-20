#!/usr/bin/env python3

from collections import Counter
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

rep = [line.split(' => ') for line in content.split('\n\n')[0].splitlines()]
molecule = content.split('\n\n')[1].strip()

res = set()
