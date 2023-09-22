#!/usr/bin/env python3

import pathlib
import re
import sys
from collections import Counter


def parse(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.splitlines():
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        data.append(((x1, y1), (x2, y2)))
    return data


def solution(data, p2=False):
    """Solve part 1."""
    grid = []
    for points in data:
        (lx, ly), (hx, hy) = sorted(points)
        if lx == hx or ly == hy:
            for x in range(lx, hx + 1):
                for y in range(ly, hy + 1):
                    grid.append((x, y))
        if p2:
            try:
                slope = (hx - lx) / (hy - ly)
                if abs(slope) == 1:
                    y = ly
                    for x in range(lx, hx + 1):
                        grid.append((x, y))
                        y += slope
            except ZeroDivisionError:
                pass

    cnt = Counter(grid)
    return sum(1 for v in cnt.values() if v >= 2)


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, p2=True)

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
