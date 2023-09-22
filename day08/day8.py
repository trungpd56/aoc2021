#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def signals(line):
    toks = [set(tok) for tok in line.split()]
    info = [set()] * 10
    for tok in toks:
        match len(tok):
            case 2:
                info[1] = tok
            case 4:
                info[4] = tok
            case 3:
                info[7] = tok
            case 7:
                info[8] = tok

    for tok in toks:
        if tok in info:
            continue
        if len(tok) == 5 and info[1] < tok:
            info[3] = tok
        if len(tok) == 6 and not info[7] < tok:
            info[6] = tok

    for tok in toks:
        if tok in info:
            continue
        if len(tok) == 5:
            if not tok < info[6]:
                info[2] = tok
            if tok < info[6]:
                info[5] = tok
        if len(tok) == 6:
            if info[3] < tok:
                info[9] = tok
            if not info[3] < tok:
                info[0] = tok

    return info


def part1(data):
    """Solve part 1."""
    cnt = 0
    for line in data:
        parts = line.split(" | ")
        for tok in parts[1].split():
            if len(tok) in [2, 4, 3, 7]:
                cnt += 1
    return cnt


def part2(data):
    """Solve part 2."""
    total = 0
    for line in data:
        parts = line.split(" | ")
        info = signals(parts[0])
        res = ""
        for tok in parts[1].split():
            res += str(info.index(set(tok)))
        total += int(res)
    return total


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
