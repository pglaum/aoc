#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

lines = content.splitlines()

def run_program(A=0, B=0):
    idx = 0
    while True:
        if idx < 0 or idx >= len(lines):
            break
        #print(idx, lines[idx].strip(), A, B)

        i = lines[idx].split(' ')[0]
        match i:
            case 'hlf':
                reg = lines[idx].split(' ')[1]
                if reg == 'a':
                    A = A // 2
                else:
                    B = B // 2
                idx += 1
            case 'tpl':
                reg = lines[idx].split(' ')[1]
                if reg == 'a':
                    A = A * 3
                else:
                    B = B * 3
                idx += 1
            case 'inc':
                reg = lines[idx].split(' ')[1]
                if reg == 'a':
                    A = A + 1
                else:
                    B = B + 1
                idx += 1
            case 'jmp':
                off = int(lines[idx].split(' ')[1])
                idx += off
            case 'jie':
                reg, off = lines[idx].split(' ')[1:]
                reg = reg[:-1]
                if reg == 'a':
                    num = A
                else:
                    num = B
                if num % 2 == 0:
                    idx += int(off)
                else:
                    idx += 1
            case 'jio':
                reg, off = lines[idx].split(' ')[1:]
                reg = reg[:-1]
                if reg == 'a':
                    num = A
                else:
                    num = B
                if num == 1:
                    idx += int(off)
                else:
                    idx += 1

    return B

print('Part 1:', run_program(0, 0))
print('Part 2:', run_program(1, 0))
