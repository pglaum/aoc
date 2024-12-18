#!/usr/bin/env python3

import os
import networkx as nx

fdir = os.path.dirname(os.path.realpath(__file__))

inputs = [
    ('example', (7,7), 12),
    ('input', (71,71), 1024),
]
use_input = inputs[1]

with open(os.path.join(fdir, use_input[0]), 'r') as f:
    content = f.read()

coords = []
for l in content.splitlines():
    i, j = [int(x) for x in l.split(',')]
    coords.append((i, j))

grid = use_input[1]

blocked = [] # coords[:use_input[2]]
start = (0, 0)
goal = (use_input[1][0] - 1, use_input[1][1] - 1)

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

G = nx.Graph()
for i in range(use_input[1][0]):
    for j in range(use_input[1][1]):
        if (i, j) in blocked:
            continue
        for d in dirs:
            n = (i + d[0], j + d[1])
            if n not in blocked:
                G.add_edge((i, j), n)
print(G)

p = nx.shortest_path_length(G, (0, 0), (use_input[1][0] - 1, use_input[1][1] - 1))
print('Part 1:', p)

G = nx.Graph()
for i in range(use_input[1][0]):
    for j in range(use_input[1][1]):
        for d in dirs:
            n = (i + d[0], j + d[1])
            G.add_edge((i, j), n)

p = []
for c in coords:
    G.remove_node(c)
    if len(p) and c not in p:
        continue

    try:
        p = nx.shortest_path(G, (0, 0), (use_input[1][0] - 1, use_input[1][1] - 1))
    except:
        print('Part 2:', ','.join([str(x) for x in c]))
        break
