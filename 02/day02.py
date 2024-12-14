#!/usr/bin/env python3

with open('input', 'r') as f:
    content = f.read()

qm = 0
ribbon = 0

for line in content.splitlines():
    l, w, h = map(int, line.split('x'))
    qm += 2 * w * h + 2 * w * l + 2 * h * l
    qm += min(w*h, w*l, h*l)

    ribbon += w * h * l
    ribbon += 2 * w + 2 * h + 2 * l - max(w, h, l) * 2

print('Part 1:', qm)
print('Part 2:', ribbon)