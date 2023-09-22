#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return [list(map(int, list(line))) for line in puzzle_input.splitlines()]


def flash(r, c, data):
    maxr = len(data)
    maxc = len(data[0])
    data[r][c] = 0
    cnt = 1
    neis = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in neis:
        if 0 <= r + dr < maxr and 0 <= c + dc < maxc and data[r + dr][c + dc] != 0:
            data[r + dr][c + dc] += 1
            if data[r + dr][c + dc] > 9:
                cnt += flash(r + dr, c + dc, data)
    return cnt


def solution(data: list, n: int = 100) -> tuple:
    """Solve part 1."""
    maxr = len(data)
    maxc = len(data[0])
    full = maxr * maxc
    total = 0
    time = 0
    while True:
        time += 1
        for r in range(maxr):
            for c in range(maxc):
                data[r][c] += 1
        cnt = 0
        for r in range(maxr):
            for c in range(maxc):
                if data[r][c] > 9:
                    cnt += flash(r, c, data)
        total += cnt
        if time == n:
            part1 = total
        if cnt == full:
            part2 = time
            return part1, part2


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
    if solution2:
        print(f" part2: {solution2}")
