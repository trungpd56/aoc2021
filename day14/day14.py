#!/usr/bin/env python3
from collections import defaultdict


def solve(pairs):
    cnt = defaultdict(int)
    for p, n in pairs.items():
        cnt[p[0]] += n
    cnt[puz[-1]] += 1
    return max(cnt.values()) - min(cnt.values())


with open('input.txt', 'r') as f:
    puz, raw = f.read().strip().split('\n\n')

info = {}
for line in raw.split('\n'):
    toks = line.split(' -> ')
    info[toks[0]] = toks[1]

pairs = defaultdict(int)
for i in range(len(puz) - 1):
    pairs[puz[i] + puz[i+1]] += 1

for i in range(40):
    if i == 10:
        part1 = solve(pairs)
    pairs2 = defaultdict(int)
    for p in pairs:
        pairs2[p[0] + info[p]] += pairs[p]
        pairs2[info[p] + p[1]] += pairs[p]
    pairs = pairs2

print(f'Part1: {part1}')
part2 = solve(pairs)
print(f'Part2: {part2}')
