import sys
from itertools import permutations

places = set()
distances = dict()
for line in open('input'):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = sys.maxsize
sd = {}
longest = 0
ld = {}
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    if dist < shortest:
        shortest = dist
        sd = items
    if dist > longest:
        longest = dist
        ld = items

print("shortest: %d" % (shortest))
print(sd)
print()
print("longest: %d" % (longest))
print(ld)
