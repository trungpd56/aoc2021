#!/usr/bin/env python3

def pgrid(g):
    maxr = len(g)
    maxc = len(g[0])
    for r in range(maxr):
        for c in range(maxc):
            print(g[r][c])
        print()


with open('input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f.readlines()]

maxr = len(grid)
maxc = len(grid[0])
t = 0
while True:
    next_grid = [row[:] for row in grid]
    for r in range(maxr):
        for c in range(maxc):
            if grid[r][c] == '>' and grid[r][(c+1) % maxc] == '.':
                next_grid[r][(c+1) % maxc] = '>'
                next_grid[r][c] = '.'
    next_grid2 = [row[:] for row in next_grid]
    for r in range(maxr):
        for c in range(maxc):
            if next_grid[r][c] == 'v' and next_grid[(r+1) % maxr][c] == '.':
                next_grid2[(r+1) % maxr][c] = 'v'
                next_grid2[r][c] = '.'
    t += 1
    if grid == next_grid2:
        break
    grid = next_grid2

print(f'Part1: {t}')
