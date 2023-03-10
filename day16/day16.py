#!/usr/bin/env python3
import math


def solve(bits):
    ver = int(bits[:3], 2)
    ptype = int(bits[3:6], 2)

    if ptype == 4:
        i = 6
        res = ''
        while True:
            res += bits[i+1:i+5]
            i += 5
            if bits[i-5] == '0':
                break
        return ver, i, int(res, 2)

    if bits[6] == '0':
        sublen = int(bits[7:22], 2)
        i = 22
        nums = []
        while i < sublen + 22:
            v, l, res = solve(bits[i:])
            i += l
            ver += v
            nums.append(res)
    else:
        numpac = int(bits[7:18], 2)
        i = 18
        nums = []
        for _ in range(numpac):
            v, l, res = solve(bits[i:])
            ver += v
            i += l
            nums.append(res)

    if ptype == 0:
        res = sum(nums)
    elif ptype == 1:
        res = math.prod(nums)
    elif ptype == 2:
        res = min(nums)
    elif ptype == 3:
        res = max(nums)
    elif ptype == 5:
        res = int(nums[0] > nums[1])
    elif ptype == 6:
        res = int(nums[0] < nums[1])
    elif ptype == 7:
        res = int(nums[0] == nums[1])
    else:
        assert False

    return ver, i, res


with open('input.txt', 'r') as f:
    data = f.read().strip()

hexa = bin(int(data, 16))[2:].zfill(len(data)*4)

part1, _, part2 = solve(hexa)
print(f'Part1: {part1}')
print(f'Part2: {part2}')
