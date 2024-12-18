#!/usr/bin/env python3

import codecs
import json
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

count = 0
count2 = 0
for line in content.splitlines():
    raw_len = len(line)
    normal_len = len(codecs.decode(line[1:-1], 'unicode_escape'))
    long_len = len(json.dumps(line))

    count += (raw_len - normal_len)
    count2 += (long_len - raw_len)

print('Part 1:', count)
print('Part 2:', count2)
