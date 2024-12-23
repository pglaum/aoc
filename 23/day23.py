#!/usr/bin/env python3

import os
import networkx as nx

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

net = {}

G = nx.Graph()

for line in content.splitlines():
    pc1, pc2 = line.split('-')
    if pc1 not in net:
        net[pc1] = set()
    if pc2 not in net:
        net[pc2] = set()
    net[pc1].add(pc2)
    net[pc2].add(pc1)
    G.add_edge(pc1, pc2)

conns = set()
for pc1 in net.keys():
    for pc2 in net[pc1]:
        if pc1 == pc2:
            continue

        for pc3 in net[pc2]:
            if pc1 == pc3 or pc2 == pc3:
                continue

            if (pc1 not in net[pc3]):
                continue

            con = tuple(sorted([pc1, pc2, pc3]))
            conns.add(con)

count = 0
for con in conns:
    for pc in con:
        if 't' == pc[0]:
            count += 1
            break

print('Part 1:', count)

longest = max(nx.find_cliques(G), key=len)

print('Part 2:', ','.join(sorted(longest)))
