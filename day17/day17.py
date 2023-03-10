#!/usr/bin/env python3
import re

with open('input.txt', 'r') as f:
    data = f.read().strip()

txmin, txmax, tymin, tymax = map(int, re.findall(r'-?\d+', data))
maxmaxy = 0
velo = set()
for DX in range(1, txmax+1):
    for DY in range(-100, 1000):
        x, y, dx, dy = 0, 0, DX, DY
        maxy = 0
        for t in range(txmax):
            x += dx
            y += dy
            dx = max(dx-1, 0)
            dy -= 1
            maxy = max(maxy, y)
            if txmin <= x <= txmax and tymin <= y <= tymax:
                velo.add((DX, DY))
                maxmaxy = max(maxy, maxmaxy)
                break
            if x > txmax:
                break
            if y < tymin and dy < 0:
                break


part1 = maxmaxy
print(f'Part1: {part1}')

part2 = len(velo)
print(f'Part2: {part2}')
