#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read().strip()

def get_length(l, r = True):
    in_marker = False
    marker = ''
    added = 0
    i = -1
    while i < len(l) - 1:
        i += 1

        #print(i, len(content))
        #print(content[i])
        if l[i] == '(':
            in_marker = True
            continue
        if l[i] == ')':
            chars, repeats = [int(x) for x in marker.split('x')]
            #print('add', chars, repeats)
            if r:
                #print(l, i, chars, l[i+1:i+1+chars], '|', marker, len(marker))
                added += get_length(l[i+1:i+1+chars]) * repeats - 2 - len(marker) - chars
            else:
                added += chars * (repeats - 1) - len(marker) - 2
            i += chars
            in_marker = False
            marker = ''
            continue
        if in_marker:
            marker += l[i]

    #print('get_length', l, len(l), added, '->', len(l) + added)
    return len(l) + added

print('Part 1:', get_length(content, False))
print('Part 2:', get_length(content))
