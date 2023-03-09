#!/usr/bin/env python3
from collections import defaultdict, deque


def low(r, c):
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < maxr and 0 <= c + dc < maxc:
            if grid[(r, c)] >= grid[(r+dr, c+dc)]:
                return False
    return True


def walk(r, c):
    queue = deque([(r, c)])
    seen = set()
    while queue:
        rn, cn = queue.popleft()
        if (rn, cn) in seen:
            pass
        seen.add((rn, cn))
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 <= rn + dr < maxr and 0 <= cn + dc < maxc:
                if (
                    (rn+dr, cn+dc) not in seen and
                    grid[(rn+dr, cn+dc)] != 9
                ):
                    queue.append((rn+dr, cn+dc))
    return len(seen)


with open('input.txt', 'r') as f:
    lines = f.readlines()

maxr = len(lines)
maxc = len(lines[0].strip())
grid = defaultdict(int)
for r, line in enumerate(lines):
    for c, char in enumerate(line.strip()):
        grid[(r, c)] = int(char)

risk = 0
points = set()
for r in range(maxr):
    for c in range(maxc):
        if low(r, c):
            risk += 1 + grid[(r, c)]
            points.add((r, c))

part1 = risk
print(f'Part1: {part1}')


basins = sorted([walk(*p) for p in points], reverse=True)
part2 = basins[0] * basins[1] * basins[2]
print(f'Part2: {part2}')
