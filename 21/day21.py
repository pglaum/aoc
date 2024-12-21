#!/usr/bin/env python3

from functools import cache
import networkx as nx
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

N = nx.Graph()

N_list = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
    ['',0,-1],
]
N.add_edge(7, 4)
N.add_edge(7, 8)
N.add_edge(8, 9)
N.add_edge(8, 5)
N.add_edge(9, 6)
N.add_edge(4, 5)
N.add_edge(4, 1)
N.add_edge(5, 2)
N.add_edge(5, 6)
N.add_edge(6, 3)
N.add_edge(1, 2)
N.add_edge(2, 0)
N.add_edge(2, 3)
N.add_edge(3, -1)
N.add_edge(0, -1)

D_list = [
    list(' ^A'),
    list('<v>'),
]
D = nx.Graph()
D.add_edge('^', 'A')
D.add_edge('^', 'v')
D.add_edge('A', '>')
D.add_edge('<', 'v')
D.add_edge('v', '>')

Np = {}
for n1 in N:
    for n2 in N:
        if n1 > n2:
            p1 = nx.all_shortest_paths(N, n1, n2)
            p2 = nx.all_shortest_paths(N, n2, n1)
            Np[(n1, n2)] = list(p1)
            Np[(n2, n1)] = list(p2)

Dp = {}
for d1 in D:
    for d2 in D:
        if d1 > d2:
            p1 = nx.all_shortest_paths(D, d1, d2)
            p2 = nx.all_shortest_paths(D, d2, d1)
            Dp[(d1, d2)] = list(p1)
            Dp[(d2, d1)] = list(p2)

dirs = {
    (1, 0): '^',
    (-1, 0): 'v',
    (0, 1): '>',
    (0, -1): '<',
}

@cache
def find_dir_N(n1, n2):
    if n1 == n2:
        return 'A'

    v1 = ()
    v2 = ()
    for i in range(len(N_list)):
        for j in range(len(N_list[i])):
            if N_list[i][j] == n1:
                v1 = (i, j)
            if N_list[i][j] == n2:
                v2 = (i, j)

    if not len(v1) or not len(v2):
        print('Not found!')
        print(n1, v1)
        print(n2, v2)

    if abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) > 1:
        print('No direct connection between', n1, n2)
        return 'X'

    return dirs[(v1[0] - v2[0], v2[1] - v1[1])]


def find_way_N(path):
    w = ''
    for i in range(len(path) - 1):
        w += find_dir_N(path[i], path[i+1])
    return w

def find_paths_N(code, start='A'):
    code = start + code
    N_paths = []
    for i in range(len(code) - 1):
        n1 = int(code[i]) if code[i] != 'A' else -1
        n2 = int(code[i+1]) if code[i+1] != 'A' else -1

        p = Np[(n1, n2)]
        np = []
        if len(N_paths) > 0:
            for ps in N_paths:
                for x in p:
                    np.append(ps + x)
            N_paths = np.copy()
        else:
            N_paths = p.copy()

    # add confirmation of last button
    for i in range(len(N_paths)):
        N_paths[i].append(N_paths[i][-1])

    return N_paths

@cache
def find_dir_D(d1, d2):
    if d1 == d2:
        return 'A'

    v1 = ()
    v2 = ()
    for i in range(len(D_list)):
        for j in range(len(D_list[i])):
            if D_list[i][j] == d1:
                v1 = (i, j)
            if D_list[i][j] == d2:
                v2 = (i, j)

    if not len(v1) or not len(v2):
        print('Not found!')
        print(d1, v1)
        print(d2, v2)

    if abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) > 1:
        print('No direct connection between', d1, d2)
        return 'X'

    return dirs[(v1[0] - v2[0], v2[1] - v1[1])]


def find_way_D(path):
    w = ''
    for i in range(len(path) - 1):
        w += find_dir_D(path[i], path[i+1])
    return w

def find_paths_D(code, start='A'):
    code = start + code
    D_paths = []
    for i in range(len(code) - 1):
        n1 = code[i]
        n2 = code[i+1]

        if n1 == n2:
            p = [[n1]]
        else:
            p = Dp[(n1, n2)]

        if len(D_paths) > 0:
            dp = []
            for ps in D_paths:
                for x in p:
                    dp.append(ps + x)
            D_paths = dp.copy()
        else:
            D_paths = p.copy()

    for i in range(len(D_paths)):
        D_paths[i].append(D_paths[i][-1])

    return D_paths

@cache
def cost_D(last_pos, move, depth=2):
    if last_pos == move:
        #print('cost_D', move, depth, '->', 1)
        return move, 1

    paths = Dp[(last_pos, move)]
    ways = []
    for p1 in paths:
        ways.append(find_way_D(p1) + 'A')

    if depth > 1:
        costs = []
        for w in ways:
            costs.append(total_cost_D(w, depth-1))
        #print('    cost_D', move, ways, depth, '->', min(costs))
        return move, min(costs)

    #print('cost_D', move, ways, depth, '->', min([len(w) for w in ways]))
    return move, min([len(w) for w in ways])

@cache
def total_cost_D(way, depth=2):
    total = 0
    last_pos = 'A'
    for i in range(len(way)):
        last_pos, cost = cost_D(last_pos, way[i], depth)
        #print('cost_D', way[i], ':', cost)
        total += cost
    return total

score = 0
for code in content.splitlines():
    final_paths = []
    N_paths = find_paths_N(code)
    #print('code:', code)
    costs = []
    for np in N_paths:
        way = find_way_N(np)
        costs.append(total_cost_D(way, 2))

    print('cost:', min(costs))
    score += min(costs) * int(code[:-1])

print('Part 1:', score)

score = 0
for code in content.splitlines():
    final_paths = []
    N_paths = find_paths_N(code)
    #print('code:', code)
    costs = []
    for np in N_paths:
        way = find_way_N(np)
        costs.append(total_cost_D(way, 25))

    print('cost:', min(costs))
    score += min(costs) * int(code[:-1])

print('Part 2:', score)
