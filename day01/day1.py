#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    cnt = 0
    for n1, n2 in zip(data, data[1:]):
        if n1 < n2:
            cnt += 1
    return cnt


def part2(data):
    """Solve part 2."""
    window = [sum((n1, n2, n3)) for n1, n2, n3 in zip(data, data[1:], data[2:])]
    return part1(window)


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
