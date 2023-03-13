#!/usr/bin/env python3

with open('ex.txt', 'r') as f:
    p1, p2 = [int(line.strip().split()[-1])-1 for line in f.readlines()]

s1, s2, rolls = 0, 0, 0
while True:
    rolls += 3
    p1 = (p1 + ((rolls-1) % 100 + 1) * 3 - 3) % 10
    s1 += p1 + 1
    if s1 >= 1000:
        print(f'Part1: {rolls * s2}')
        break

    rolls += 3
    p2 = (p2 + ((rolls-1) % 100 + 1) * 3 - 3) % 10
    s2 += p2 + 1
    if s2 >= 1000:
        print(f'Part1: {rolls * s1}')
        break


part1 = ""
print(f'Part1: {part1}')

part2 = ""
print(f'Part2: {part2}')
