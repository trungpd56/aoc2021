#!/usr/bin/env python3

import pathlib
import sys
from heapq import heappop, heappush


def parse(puzzle_input):
    """Parse input."""
    return [list(map(int, list(line))) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    maxr = len(data)
    maxc = len(data[0])
    neis = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    end = (maxr - 1, maxc - 1)
    queue = []
    heappush(queue, (0, 0, 0))
    seen = set()
    while True:
        risk, r, c = heappop(queue)
        if (r, c) == end:
            return risk
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in neis:
            if 0 <= r + dr < maxr and 0 <= c + dc < maxc:
                heappush(queue, (risk + data[r + dr][c + dc], r + dr, c + dc))


def genmap(data):
    maxr, maxc = len(data), len(data[0])
    maxrr, maxcc = maxr * 5, maxc * 5
    gmap = [[0 for _ in range(maxcc)] for _ in range(maxrr)]
    for r in range(maxrr):
        for c in range(maxcc):
            gmap[r][c] = data[r % maxr][c % maxc] + (r // maxr) + (c // maxc)
            if gmap[r][c] > 9:
                gmap[r][c] -= 9
    return gmap


def part2(data):
    """Solve part 2."""
    gmap = genmap(data)
    return part1(gmap)


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
