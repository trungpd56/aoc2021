#!/usr/bin/env python3

import pathlib
import sys
from typing import Tuple
import math


def parse(puzzle_input):
    """Parse input."""
    return format(int(puzzle_input, 16), f"0{len(puzzle_input)*4}b")


def decode(rep: str) -> Tuple[int, int, int]:
    ver = int(rep[:3], 2)
    ptyp = int(rep[3:6], 2)
    if ptyp == 4:
        i = 6
        res = ""
        while True:
            res += rep[i + 1 : i + 5]
            i += 5
            if rep[i - 5] == "0":
                break
        return ver, i, int(res, 2)
    if ptyp != 4:
        if rep[6] == "0":
            sublen = int(rep[7:22], 2)
            i = 22
            nums = []
            while i < sublen + 22:
                v, l, res = decode(rep[i:])
                ver += v
                i += l
                nums.append(res)
        else:
            npack = int(rep[7:18], 2)
            i = 18
            nums = []
            for _ in range(npack):
                v, l, res = decode(rep[i:])
                ver += v
                i += l
                nums.append(res)
        match ptyp:
            case 0:
                res = sum(nums)
            case 1:
                res = math.prod(nums)
            case 2:
                res = min(nums)
            case 3:
                res = max(nums)
            case 5:
                res = int(nums[0] > nums[1])
            case 6:
                res = int(nums[0] < nums[1])
            case 7:
                res = int(nums[0] == nums[1])
            case _:
                assert False

        return ver, i, res


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = decode(data)[0]
    solution2 = decode(data)[2]

    return solution1, solution2


if __name__ == "__main__":
    infile = (
        sys.argv[1]
        if len(sys.argv) > 1
        else pathlib.Path(__file__).parent / "input.txt"
    )
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
