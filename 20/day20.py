#!/usr/bin/env python3

from collections import Counter
import networkx as nx
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

lines = content.splitlines()

G = nx.Graph()

walls = []
dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
start = ()
end = ()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            if i > 0 and j > 0 and i < len(lines) - 1 and j < len(lines) - 1:
                walls.append((i, j))
            continue

        if lines[i][j] == 'S':
            start = (i, j)
        if lines[i][j] == 'E':
            end = (i, j)

        for d in dirs:
            ni = i + d[0]
            nj = j + d[1]
            if lines[ni][nj] != '#':
                G.add_edge((i, j), (ni, nj))

shortest_paths = nx.shortest_path_length(G, target=end)

def get_reachable(node, max_dist):
    reachable = []
    for dx in range(-max_dist, max_dist + 1):
        remaining = max_dist - abs(dx)
        for dy in range(-remaining, remaining + 1):
            if dx == dy == 0:
                continue
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]) and lines[nx][ny] in '.SE':
                reachable.append((nx, ny))

    return reachable

def solve(cheat_size):
    res = 0
    for node in G.nodes:
        reachable = get_reachable(node, cheat_size)

        i, j = node
        for dx, dy in reachable:
            cost = abs(i - dx) + abs(j - dy)
            savings = shortest_paths[(i, j)] - (shortest_paths[(dx, dy)] + cost)
            if savings >= 100:
                res += 1

    return res

print('Part 1:', solve(2))
print('Part 1:', solve(20))
