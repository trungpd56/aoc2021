#!/usr/bin/env python3

import pathlib
import sys
from collections import Counter


def parse(puzzle_input):
    """Parse input."""
    return [int(n) for n in puzzle_input.split(",")]


def solution(data: list, times: int = 18) -> int:
    """Solve part 1."""
    cnt = Counter(data)
    for _ in range(times):
        for n in sorted(cnt):
            cnt[n - 1] = cnt[n]
            cnt[n] = 0
        cnt[8] += cnt[-1]
        cnt[6] += cnt[-1]
        cnt[-1] = 0
    return sum(v for v in cnt.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data, times=80)
    solution2 = solution(data, times=256)
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
