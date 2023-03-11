#!/usr/bin/env python3


def pgrid(grid):
    maxr = max(p[1] for p in grid)
    maxc = max(p[0] for p in grid)
    for r in range(maxr+1):
        for c in range(maxc+1):
            if (c, r) in grid:
                print('#', end='')
            else:
                print(" ", end='')
        print()


with open('input.txt', 'r') as f:
    raw, req = f.read().strip().split('\n\n')

grid = set()
for line in raw.split('\n'):
    dot = tuple(map(int, line.split(',')))
    grid.add(dot)

for i, r in enumerate(req.split('\n')):
    if i == 1:
        # pgrid(grid)
        part1 = len(grid)
    grid2 = set()
    axis, v = r.split()[-1].split('=')
    v = int(v)
    if axis == 'y':
        grid2 = {(x, y) if y < v else (x, 2*v-y) for x, y in grid}
    if axis == 'x':
        grid2 = {(x, y) if x < v else (2*v-x, y) for x, y in grid}
    grid = grid2


print(f'Part1: {part1}')
print('Part2: ')
pgrid(grid)
