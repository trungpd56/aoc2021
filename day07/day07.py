#!/usr/bin/env python3


def score(x, y):
    n = abs(x-y) + 1
    return (n / 2) * abs(x - y)


with open('input.txt', 'r') as f:
    nums = [int(n) for n in f.read().strip().split(',')]


part1 = min([sum(abs(n-i) for n in nums) for i in range(max(nums)+1)])
print(f'Part1: {part1}')

part2 = min([sum(score(i, n) for n in nums) for i in range(max(nums)+1)])
print(f'Part2: {part2}')
