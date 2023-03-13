#!/usr/bin/env python3
from collections import Counter


def rating(nums, n=0, least=False):
    if len(nums) == 1:
        return str(nums[0][n:])
    comb = list(zip(*nums))
    common = [Counter(i).most_common() for i in comb][n]
    common = sorted(common, key=lambda x: (x[1], x[0]), reverse=True)[least][0]
    return '' + str(common) + rating([i for i in nums if i[n] == common], n+1, least)


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

combine = list(zip(*lines))
gamma = ''.join([Counter(i).most_common()[0][0] for i in combine])
epsilon = ''.join([Counter(i).most_common()[1][0] for i in combine])

part1 = int(gamma, 2) * int(epsilon, 2)
print(f'Part1: {part1}')

oxy = rating(lines)
co = rating(lines, least=True)
part2 = int(oxy, 2) * int(co, 2)
print(f'Part2: {part2}')
