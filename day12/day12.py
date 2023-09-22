#!/usr/bin/env python3

import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input):
    """Parse input."""
    info = defaultdict(list)
    for line in puzzle_input.splitlines():
        toks = line.split("-")
        if toks[0] != "end" and toks[1] != "start":
            info[toks[0]].append(toks[1])
        if toks[1] != "end" and toks[0] != "start":
            info[toks[1]].append(toks[0])
    return info


def solution(visited: list, info: dict) -> int:
    if visited[-1] == "end":
        return 1
    cnt = 0
    for path in info[visited[-1]]:
        if path == path.lower() and path in visited:
            continue
        nvisited = visited + [path]
        cnt += solution(nvisited, info)
    return cnt


def solution2(visited: list, info: dict, done: bool = False) -> int:
    if visited[-1] == "end":
        return 1
    cnt = 0
    for path in info[visited[-1]]:
        if path == path.upper() or path not in visited:
            cnt += solution2(visited + [path], info, done)
        elif path == path.lower() and path in visited:
            if not done:
                cnt += solution2(visited + [path], info, True)
            else:
                continue
    return cnt


def part1(data):
    """Solve part 1."""
    return solution(visited=["start"], info=data)


def part2(data):
    """Solve part 2."""
    return solution2(visited=["start"], info=data)


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
