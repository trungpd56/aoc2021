#!/usr/bin/env python3

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    pos = 0
    depth = 0
    for line in data:
        cmd, n = line.split()
        n = int(n)
        match cmd:
            case 'forward':
                pos += n
            case 'down':
                depth += n
            case 'up':
                depth -= n
            case _:
                assert False
    return pos * depth
        

def part2(data):
    """Solve part 2."""
    pos = 0
    depth = 0
    aim = 0
    for line in data:
        cmd, n = line.split()
        n = int(n)
        match cmd:
            case 'forward':
                pos += n
                depth += aim * n
            case 'down':
                aim += n
            case 'up':
                aim -= n
            case _:
                assert False
    return pos * depth

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent / "input.txt"
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
