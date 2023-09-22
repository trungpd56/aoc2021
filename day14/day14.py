#!/usr/bin/env python3

import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input):
    """Parse input."""
    temp, raw = puzzle_input.split("\n\n")
    info = {}
    for line in raw.split("\n"):
        toks = line.split(" -> ")
        info[toks[0]] = toks[1]
    return temp, info


def solution(data: tuple, n: int = 10) -> int:
    """Solve part 1."""
    temp, info = data
    cnt = defaultdict(int)
    for i in range(1, len(temp)):
        cnt[temp[i - 1] + temp[i]] += 1
    for _ in range(n):
        ncnt = defaultdict(int)
        for k in cnt:
            ncnt[k[0] + info[k]] += cnt[k]
            ncnt[info[k] + k[1]] += cnt[k]
        cnt = ncnt
    res = defaultdict(int)
    for k in cnt:
        res[k[0]] += cnt[k]
    res[temp[-1]] += 1
    snum = sorted(res.values())
    return snum[-1] - snum[0]


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, n=40)

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
