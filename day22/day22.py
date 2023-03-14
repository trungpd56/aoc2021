#!/usr/bin/env python3
import re
from collections import defaultdict


with open('input.txt', 'r') as f:
    lines = f.readlines()

lights = defaultdict(int)
for line in lines:
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r'-?\d+', line))
    if (
        -50 <= x1 <= 50 and
        -50 <= x2 <= 50 and
        -50 <= y1 <= 50 and
        -50 <= y2 <= 50 and
        -50 <= z1 <= 50 and
        -50 <= z2 <= 50
    ):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    if line.startswith('on'):
                        lights[(x, y, z)] = 1
                    if line.startswith('off'):
                        lights[(x, y, z)] = 0

part1 = sum(lights.values())
print(f'Part1: {part1}')


part2 = ""
print(f'Part2: {part2}')
