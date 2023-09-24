#!/usr/bin/env python3

import pathlib
import sys
import re
from typing import Tuple


def parse(puzzle_input: str) -> Tuple[int, int, int, int]:
    """Parse input."""
    MINX, MAXX, MINY, MAXY = tuple(map(int, re.findall(r"-?\d+", puzzle_input)))
    return MINX, MAXX, MINY, MAXY


def solution(data: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Solve part 1."""
    MINX, MAXX, MINY, MAXY = data
    maxyy = 0
    vlist = []
    for DX in range(0, MAXX+1):
        for DY in range(MINY, 500):
            x, y = (0, 0)
            dx = DX
            dy = DY
            maxy = 0
            while True:
                x += dx
                y += dy
                dx = max(0, dx - 1)
                dy -= 1
                maxy = max(y, maxy)
                if MINX <= x <= MAXX and MINY <= y <= MAXY:
                    maxyy = max(maxyy, maxy)
                    vlist.append((DX, DY))
                    break
                if x > MAXX:
                    break
                if dy < 0 and y < MINY:
                    break
    return maxyy, len(vlist)



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
