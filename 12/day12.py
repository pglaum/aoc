#!/usr/bin/env python3

import json
import os
import re

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read().strip()

numbers = re.findall(r"-?\d+", content)
print('Part 1:', sum([int(x) for x in numbers]))

obj = json.loads(content)

def search(obj):
    res = 0
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, dict):
                if 'red' in i.values():
                    continue
                else:
                    res += search(i)
            if isinstance(i, list):
                res += search(i)
            if isinstance(i, int):
                res += i
    elif isinstance(obj, dict):
        for k, i in obj.items():
            if isinstance(i, dict):
                if 'red' in i.values():
                    continue
                else:
                    res += search(i)
            if isinstance(i, list):
                res += search(i)
            if isinstance(i, int):
                res += i
    else:
        print(type(obj))

    return res

print('Part 2:', search(obj))
