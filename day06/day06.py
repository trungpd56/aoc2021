#!/usr/bin/env python3
from collections import Counter

with open('input.txt', 'r') as f:
    nums = Counter([int(line) for line in f.read().strip().split(',')])

for i in range(256):
    if i == 80:
        part1 = sum(nums.values())
    nums1 = Counter()
    for n in nums:
        if n-1 >= 0:
            nums1[n-1] += nums[n]
        else:
            nums1[6] += nums[n]
            nums1[8] += nums[n]
    nums = nums1

print(f'Part1: {part1}')
part2 = sum(nums.values())
print(f'Part2: {part2}')
