#!/usr/bin/env python3
from collections import defaultdict, Counter

with open('input.txt', 'r') as f:
    lines = f.readlines()

grid = []
for line in lines:
    toks = line.split(' -> ')
    p0 = tuple(map(int, toks[0].split(',')))
    p1 = tuple(map(int, toks[1].split(',')))
    ps = sorted((p0, p1))
    grid.append(ps)

cnt = defaultdict(int)
ps2 = []
for p0, p1 in grid:
    if p0[0] == p1[0] or p0[1] == p1[1]:
        for y in range(p0[1], p1[1] + 1):
            for x in range(p0[0], p1[0] + 1):
                cnt[(x, y)] += 1
                ps2.append((x, y))
    slope = (p1[1] - p0[1]) // (p1[0] - p0[0]) if p1[0] != p0[0] else None
    if slope == 1 or slope == -1:
        ps2.extend([(p0[0]+i, p0[1]+(i*slope)) for i in range(p1[0] - p0[0] + 1)])


part1 = sum([1 for n in cnt.values() if n >= 2])
print(f'Part1: {part1}')

part2 = sum(1 for i in Counter(ps2).values() if i >= 2)
print(f'Part2: {part2}')
