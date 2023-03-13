#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    nums = [int(line) for line in f.readlines()]

part1 = sum(1 for x, y in zip(nums[1:], nums) if x > y)
print(f'Part1: {part1}')

measure = [sum(n) for n in zip(nums[2:], nums[1:], nums)]
part2 = sum(1 for x, y in zip(measure[1:], measure) if x > y)
print(f'Part2: {part2}')
