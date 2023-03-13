#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.readlines()

pos = 0
depth = 0
aim = 0
pos2 = 0
depth2 = 0
for line in lines:
    toks = line.strip().split()
    n = int(toks[1])
    if toks[0] == 'forward':
        pos += n
        depth2 += aim*n
    elif toks[0] == 'down':
        depth += n
        aim += n
    elif toks[0] == 'up':
        depth -= n
        aim -= n
    else:
        assert False

part1 = pos * depth
print(f'Part1: {part1}')
part2 = pos * depth2
print(f'Part2: {part2}')
