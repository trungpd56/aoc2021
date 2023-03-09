#!/usr/bin/env python3
from collections import defaultdict


def walk(visited):
    if visited[-1] == 'end':
        # print(visited)
        return 1
    cnt = 0
    for cave in info[visited[-1]]:
        if cave.lower() in visited:
            pass
        else:
            cnt += walk(visited + [cave])
    return cnt


def walk2(visited, small=False):
    if visited[-1] == 'end':
        # print(visited)
        return 1
    cnt = 0
    for cave in info[visited[-1]]:
        if cave.lower() not in visited:
            cnt += walk2(visited + [cave], small)
        elif cave.upper() in visited:
            cnt += walk2(visited + [cave], small)
        if cave.lower() in visited and not small:
            cnt += walk2(visited+[cave], small=True)

    return cnt


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = defaultdict(list)
for line in lines:
    toks = line.strip().split('-')
    if toks[1] != 'start':
        info[toks[0]].append(toks[1])
    if toks[1] != 'end' and toks[0] != 'start':
        info[toks[1]].append(toks[0])

part1 = walk(['start'])
print(f'Part1: {part1}')

part2 = walk2(['start'])
print(f'Part2: {part2}')
