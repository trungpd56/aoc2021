#!/usr/bin/env python3


def flash(r, c):
    cnt = 1
    grid[(r, c)] = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (
                0 <= r+dr < maxr and
                0 <= c+dc < maxc and
                grid[(r+dr, c+dc)] != 0
            ):
                grid[(r+dr, c+dc)] += 1
                if grid[(r+dr, c+dc)] > 9:
                    cnt += flash(r+dr, c+dc)
    return cnt


def pgrid(grid):
    for r, c in grid:
        print(grid[(r, c)], end='')
        if c == maxc-1:
            print()


with open('input.txt', 'r') as f:
    lines = f.readlines()

maxr = len(lines)
maxc = len(lines[0].strip())
grid = {}
for r, line in enumerate(lines):
    for c, char in enumerate(line.strip()):
        grid[(r, c)] = int(char)

numb_flashes = 0
n = 0
while True:
    nflash = 0
    if n == 100:
        part1 = numb_flashes
    for r, c in grid:
        grid[(r, c)] += 1
    for r, c in grid:
        if grid[(r, c)] > 9:
            nflash += flash(r, c)
    numb_flashes += nflash
    if nflash == maxc*maxr:
        part2 = n + 1
        break
    n += 1

print(f'Part1: {part1}')
print(f'Part2: {part2}')
