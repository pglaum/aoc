#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

def exec():
    while len(unvisited):
        r = None
        visited = False

        for r in unvisited:
            e = registers[r]['e']
            if len(e) == 1:
                if e[0].isnumeric():
                    if registers[r]['v'] is not None:
                        print('skipping value assignment')
                        continue
                    registers[r]['v'] = int(e[0])
                    visited = True
                    break
                else:
                    if registers[e[0]]['v'] is not None:
                        registers[r]['v'] = registers[e[0]]['v']
                        visited = True
                        break
                    else:
                        continue

            if len(e) == 2:
                if e[0] == 'NOT':
                    if registers[e[1]]['v'] == None:
                        continue
                    else:
                        registers[r]['v'] = ~registers[e[1]]['v']
                        visited = True
                        break
                else:
                    print('unexpected expression 2', e)

            if len(e) == 3:
                if e[0].isnumeric():
                    p1 = int(e[0])
                else:
                    p1 = registers[e[0]]['v']

                if e[2].isnumeric():
                    p2 = int(e[2])
                else:
                    p2 = registers[e[2]]['v']

                if p1 is None or p2 is None:
                    continue

                try:
                    match e[1]:
                        case 'AND':
                            registers[r]['v'] = p1 & p2
                            visited = True
                            break
                        case 'OR':
                            registers[r]['v'] = p1 | p2
                            visited = True
                            break
                        case 'LSHIFT':
                            registers[r]['v'] = p1 << p2
                            visited = True
                            break
                        case 'RSHIFT':
                            registers[r]['v'] = p1 >> p2
                            visited = True
                            break
                        case _:
                            print('unexpected expression 3', e)
                except Exception as ex:
                    print(ex)
                    print(e, p1, p2)
                    exit(1)

                if visited:
                    break

        if visited:
            unvisited.remove(r)


registers = {}
unvisited = []

for l in content.splitlines():
    r = l.split('-> ')[1]
    expr = l.split(' ->')[0].split(' ')
    registers[r] = {
        'v': None,
        'e': expr
    }
    unvisited.append(r)

exec()
res = registers['a']['v']
print('Part 1:', registers['a']['v'])

for r in registers.keys():
    registers[r]['v'] = None
    unvisited.append(r)
registers['b']['e'] = (str(res),)

exec()
print('Part 2:', registers['a']['v'])
