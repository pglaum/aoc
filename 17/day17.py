#!/usr/bin/env python3

import math
import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()

class Computer:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.operations = []

    def run_operations(self, with_checks=False):
        outputs = []
        instruction_pointer = 0
        while instruction_pointer < len(self.operations):
            op = self.operations[instruction_pointer]
            param = self.operations[instruction_pointer + 1]

            combo_operand = param
            if param == 4:
                combo_operand = self.A
            elif param == 5:
                combo_operand = self.B
            elif param == 6:
                combo_operand = self.C
            elif param == 7:
                print('Unexpected combo operand')

            if op == 0:
                self.A = self.A // (2 ** combo_operand)
            elif op == 1:
                self.B = self.B ^ param
            elif op == 2:
                self.B = combo_operand % 8
            elif op == 3:
                if self.A != 0:
                    instruction_pointer = param - 2
            elif op == 4:
                self.B = self.B ^ self.C
            elif op == 5:
                outputs.append(combo_operand % 8)
            elif op == 6:
                self.B = self.A // (2 ** combo_operand)
            elif op == 7:
                self.C = self.A // (2 ** combo_operand)

            #print('Operation', instruction_pointer, op, param, combo_operand)
            #self.print()
            #print()

            instruction_pointer += 2

        if with_checks:
            return outputs

        print('Operation outputs:', ','.join([str(x) for x in outputs]))

    def parse(self, content: str):
        for i, line in enumerate(content.splitlines()):
            if i == 0:
                self.A = int(line.split(': ')[1])
            if i == 1:
                self.B = int(line.split(': ')[1])
            if i == 2:
                self.C = int(line.split(': ')[1])

            if line.startswith('Program'):
                self.operations = [int(x) for x in line.split(': ')[1].split(',')]

    def print(self):
        print(f'Registers: {self.A} | {self.B} | {self.C}')
        print(f'Operations: {self.operations}')

computer = Computer()
computer.parse(content)
computer.print()

print()
print('Part 1')
computer.run_operations()
computer.print()

print()
print('Part 2')

valid = [0]
for length in range(1, len(computer.operations)+1):
    oldvalid = valid
    valid = []
    for num in oldvalid:
        for offset in range(8):
            newnum = 8*num + offset
            computer.A = newnum
            computer.B = 0
            computer.C = 0
            operations = computer.run_operations(True)
            if operations == computer.operations[-length:]:
                valid.append(newnum)

print(min(valid))
