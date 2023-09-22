#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    grid, insts = puzzle_input.split("\n\n")
    grid = {tuple(map(int, line.split(","))) for line in grid.split("\n")}
    return grid, insts.splitlines()


def solution(data):
    """Solve part 1."""
    grid = data[0]
    for i, line in enumerate(data[1]):
        if i == 1:
            part1 = len(grid)
        axis, n = line.split()[-1].split("=")
        n = int(n)
        match axis:
            case "y":
                grid = {(x, y) if y < n else (x, 2 * n - y) for x, y in grid}
            case "x":
                grid = {(x, y) if x < n else (2 * n - x, y) for x, y in grid}
                pass
            case _:
                assert False
    display = ""
    maxy = max(y for _, y in grid) + 1
    maxx = max(x for x, _ in grid) + 1
    for y in range(maxy):
        for x in range(maxx):
            display += "#" if (x, y) in grid else "."
        display += "\n"
    print()
    print(display)
    return part1, display


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1, solution2 = solution(data)

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
