#!/usr/bin/env python3

import enum
import os
import heapq

from collections import defaultdict
fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

def dijkstra_paths(graph, start, end_nodes):
    all_shortest_paths = []
    min_cost = float('inf')

    pq = [(0, start, [start])]

    path_costs = defaultdict(lambda: float('inf'))
    path_costs[start] = 0

    while pq:
        cost, current_node, path = heapq.heappop(pq)

        if cost > min_cost:
            break

        if current_node in end_nodes:
            if cost < min_cost:
                min_cost = cost
                all_shortest_paths = [path]
            elif cost == min_cost:
                all_shortest_paths.append(path)

            continue

        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            if new_cost < path_costs[neighbor]:
                path_costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
            elif new_cost == path_costs[neighbor]:
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return all_shortest_paths, min_cost

def parse(cnt):
    grid = {
        (y, x): c
        for y, l in enumerate(cnt.splitlines())
        for x, c in enumerate(l)
    }

    graph = defaultdict(dict)
    for n in grid:
        if grid[n] != '#':
            graph[(n, True)][(n, False)] = 1000
            graph[(n, False)][(n, True)] = 1000
            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if grid[(n[0] + dy, n[1] + dx)] != '#':
                    graph[(n, bool(dx))][((n[0] + dy, n[1] + dx), bool(dx))] = 1

    return graph, next(m for m in grid if grid[m] == 'S'), next(m for m in grid if grid[m] == 'E')

graph, start, end = parse(content)
shortest_path = dijkstra_paths(graph, (start, True), [(end, True), (end, False)])
print('Part 1:', shortest_path[1])


graph, start, end = parse(content)
shortest_path = dijkstra_paths(graph, (start, True), [(end, True), (end, False)])
print('Part 2:', len({e[0] for path in shortest_path[0] for e in path}))
