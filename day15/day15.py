#!/usr/bin/env python3
from heapq import heappop, heappush
from collections import defaultdict


def walk(r, c, g):
    queue = []
    maxr = max(g[0] for g in g)
    maxc = max(g[1] for g in g)
    end = (maxr, maxc)
    heappush(queue, (0, r, c))
    seen = set()
    while queue:
        risk, r, c = heappop(queue)
        if (r, c) == end:
            return risk
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 <= r+dr <= maxr and 0 <= c+dc <= maxc and not (dr == dc == 0):
                heappush(queue, (risk + g[r+dr, c+dc], r+dr, c+dc))


with open('input.txt', 'r') as f:
    lines = f.readlines()

grid = {}
for r, line in enumerate(lines):
    for c, char in enumerate(line.strip()):
        grid[(r, c)] = int(char)


part1 = walk(0, 0, grid)
print(f'Part1: {part1}')

maxr1 = max(g[0] for g in grid) + 1
maxc1 = max(g[1] for g in grid) + 1
maxr2 = maxr1 * 5
maxc2 = maxc1 * 5
grid2 = defaultdict(int)
for r in range(maxr2):
    for c in range(maxc2):
        grid2[(r, c)] = grid[(r % maxr1, c % maxc1)] + (r // maxr1) + (c // maxc1)
        if grid2[(r, c)] > 9:
            grid2[(r, c)] -= 9


part2 = walk(0, 0, grid2)
print(f'Part2: {part2}')
