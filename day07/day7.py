#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return [int(n) for n in puzzle_input.split(",")]


def part1(data):
    """Solve part 1."""
    maxn = max(data)
    fuels = [sum([abs(n - i) for n in data]) for i in range(maxn + 1)]
    return min(fuels)


def cal(x, y):
    n = abs(x - y)
    return n * (n + 1) // 2


def part2(data):
    """Solve part 2."""
    maxn = max(data)
    fuels = [sum([cal(n, i) for n in data]) for i in range(maxn + 1)]
    return min(fuels)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

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
