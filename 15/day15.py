#!/usr/bin/env python3

import os
from traceback import walk_stack

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

warehouse = [list(x) for x in content.split('\n\n')[0].splitlines()]
movements = content.split('\n\n')[1].splitlines()
pos = (0, 0)

for i, line in enumerate(warehouse):
    for j, c in enumerate(line):
        if c == '@':
            pos = (i, j)
            warehouse[i][j] = '.'

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0),
}

for l in movements:
    for c in l:
        # print(c, dirs[c])
        d = dirs[c]
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if warehouse[new_pos[0]][new_pos[1]] == '#':
            # print('hit wall')
            continue

        boxes = 0
        valid = True
        if warehouse[new_pos[0]][new_pos[1]] == 'O':
            boxes = 1
            np = new_pos
            while True:
                np = (np[0] + d[0], np[1] + d[1])
                if warehouse[np[0]][np[1]] == '.':
                    valid = True
                    break
                elif warehouse[np[0]][np[1]] == '#':
                    # print('hit wall')
                    valid = False
                    break
                elif warehouse[np[0]][np[1]] == 'O':
                    boxes += 1
                    continue
                else:
                    print('unexpected warehouse char', warehouse[np[0]][np[1]])

        if not valid:
            continue

        if boxes > 0:
            # print('Changing', warehouse[pos[0] + d[0] * (1 + boxes)][pos[1] + d[1] * (1 + boxes)], 'to a box')
            warehouse[new_pos[0]][new_pos[1]] = '.'
            warehouse[pos[0] + d[0] * (1 + boxes)][pos[1] + d[1] * (1 + boxes)] = 'O'

        pos = new_pos
        # print(pos)

score = 0
count = 0
for i, line in enumerate(warehouse):
    for j, char in enumerate(line):
        if char == 'O':
            score += i * 100 + j
            count += 1

print('Part 1:', score, count)


class Wall:
    def __init__(self, pos):
        self.pos = pos

    def on(self, checks: list[tuple[int]]):
        return self.pos in checks

class Box:
    def __init__(self, pos, warehouse):
        self.id = pos[0] * 1000 + pos[1]
        self.pos = pos
        self.warehouse = warehouse

    def can_move(self, d: tuple[int]):
        checks = [
            (self.pos[0] + d[0], self.pos[1] + d[1]),
            (self.pos[0] + d[0], self.pos[1] + d[1] + 1),
        ]
        for wall in self.warehouse.walls:
            if wall.on(checks):
                # print('wall on box checks')
                return False

        for box in self.warehouse.boxes:
            if box.id != self.id and box.on(checks):
                if not box.can_move(d):
                    return False

        return True

    def move(self, d: tuple[int]):
        # print('box.move', self.id, d)
        self.pos = (self.pos[0] + d[0], self.pos[1] + d[1])

        checks = [
            (self.pos[0], self.pos[1]),
            (self.pos[0], self.pos[1] + 1),
        ]
        for box in self.warehouse.boxes:
            if box.id != self.id and box.on(checks):
                box.move(d)

    def on(self, checks: list[tuple[int]]):
        self_checks = [
            (self.pos[0], self.pos[1]),
            (self.pos[0], self.pos[1] + 1),
        ]

        for check in checks:
            if check in self_checks:
                return True

        return False

class Warehouse:
    def __init__(self, walls, boxes, pos, movements):
        self.boxes = boxes
        self.walls = walls
        self.pos = pos
        self.movements = movements

    def move(self):
        for l in movements:
            for m in l:
                d = dirs[m]
                if self.can_move(d):
                    self.pos = (self.pos[0] + d[0], self.pos[1] + d[1])
                    for box in self.boxes:
                        if box.on([self.pos]):
                            box.move(d)
                    #print('moving', m, d, self.pos)
                #else:
                    #print('cannot move to', m, d, self.pos)

                #self.print()

    def can_move(self, d: tuple[int]):
        n = (self.pos[0] + d[0], self.pos[1] + d[1])
        for wall in self.walls:
            if wall.on([n]):
                return False
        for box in self.boxes:
            if box.on([n]):
                return box.can_move(d)

        return True

    def print(self):
        for i in range(len(content.split('\n\n')[0].splitlines())):
            s = ''
            for j in range(len(content.splitlines()[0]) * 2):
                found = False
                for w in self.walls:
                    if w.on([(i, j)]):
                        s += '#'
                        found = True
                        break
                for b in self.boxes:
                    if b.on([(i, j)]):
                        s += '█'
                        if found:
                            print('Error! overlap')
                        found = True
                        break

                if self.pos == (i, j):
                    if found:
                        print('Error! overlap')
                    s += '@'
                elif not found:
                    s += '.'

            print(s)

    def score(self):
        s = 0
        for b in self.boxes:
            s += b.pos[0] * 100 + b.pos[1]

        print('Part 2:', s)

walls = []
boxes = []
pos = (0, 0)
warehouse = Warehouse(walls, boxes, pos, movements)

for i, line in enumerate([list(x) for x in content.split('\n\n')[0].splitlines()]):
    for j, c in enumerate(line):
        if c == '#':
            warehouse.walls.append(Wall((i, j * 2)))
            warehouse.walls.append(Wall((i, j * 2 + 1)))
        if c == 'O':
            warehouse.boxes.append(Box((i, j * 2), warehouse))
        if c == '@':
            warehouse.pos = (i, j * 2)

#print('walls', [w.pos for w in warehouse.walls])
#print('boxes', [b.pos for b in warehouse.boxes])
#warehouse.print()
warehouse.move()
#warehouse.print()
warehouse.score()
