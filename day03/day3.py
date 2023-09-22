#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    cols = list(zip(*data))
    gamma = "".join([max(("0", "1"), key=lambda x: col.count(x)) for col in cols])
    epsilon = "".join([min(("0", "1"), key=lambda x: col.count(x)) for col in cols])
    return int(gamma, 2) * int(epsilon, 2)


def rating(data: list, most: bool=False) -> str:
    rating = ""
    done = len(data[0])
    i = 0
    while len(rating) < done:
        if len(data) == 1:
            return rating + data[0][i:]
        col = list(zip(*[d[i] for d in data]))[0]
        bit = sorted(("0", "1"), key=lambda x: (col.count(x), x))[most]
        data = [d for d in data if d[i] == bit]
        rating += bit
        i += 1
    return rating


def part2(data):
    """Solve part 2."""
    oxy = rating(data, most=True)
    co2 = rating(data)
    return int(oxy, 2) * int(co2, 2)


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
