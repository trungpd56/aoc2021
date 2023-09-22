#!/usr/bin/env python3

import pathlib
import sys
from collections import deque
import math


def parse(puzzle_input):
    """Parse input."""
    return [list(map(int, list(line))) for line in puzzle_input.splitlines()]


def is_low(r, c, data):
    neis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maxr = len(data)
    maxc = len(data[0])
    if all(
        data[r][c] < data[r + dr][c + dc]
        for dr, dc in neis
        if 0 <= r + dr < maxr and 0 <= c + dc < maxc
    ):
        return True
    return False


def part1(data):
    """Solve part 1."""
    cnt = 0
    low_points = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if is_low(r, c, data):
                cnt += data[r][c] + 1
                low_points.add((r, c))
    return cnt, low_points


def basin(points, data):
    neis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maxr = len(data)
    maxc = len(data[0])
    queue = deque([points])
    seen = set()
    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in neis:
            if 0 <= r + dr < maxr and 0 <= c + dc < maxc:
                if 0 <= data[r + dr][c + dc] < 9 and (r + dr, c + dc) not in seen:
                    queue.append((r + dr, c + dc))
    return len(seen)


def part2(data):
    """Solve part 2."""
    _, low_points = part1(data)
    cnt = []
    for p in low_points:
        cnt.append(basin(p, data))
    return math.prod(sorted(cnt, reverse=True)[:3])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1, _ = part1(data)
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
