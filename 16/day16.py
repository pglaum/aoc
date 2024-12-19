#!/usr/bin/env python3

import os
from os.path import samefile

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

req = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def check_sue(items, new_test = False):
    for i in items:
        if new_test:
            if i[0] in ['cats', 'trees']:
                if int(i[1]) <= req[i[0]]:
                    return False
            elif i[1] in ['pomeranians', 'goldfish']:
                if int(i[1]) >= req[i[0]]:
                    return False
            else:
                if int(i[1]) != req[i[0]]:
                    return False
        else:
            if int(i[1]) != req[i[0]]:
                return False

    return True

sues = {}
for line in content.splitlines():
    sue = line.split(':')[0].split()[-1]
    item_str = (':'.join(line.split(':')[1:])).split(',')
    items = [[x.strip() for x in i.split(':')] for i in item_str]
    sues[sue] = items

    if check_sue(items):
        print('Part 1:', sue)

    if check_sue(items, True):
        print('Part 2:', sue)
