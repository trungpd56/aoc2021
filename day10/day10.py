#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def check(line):
    pairs = []
    info = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    for c in line:
        if c in "([{<":
            pairs.append(c)
        else:
            if c in info.values() and info[pairs[-1]] == c:
                pairs.pop()
            else:
                return False, c
    reverse_pair = [info[c] for c in pairs[::-1]]
    return True, "".join(reverse_pair)


def part1(data):
    """Solve part 1."""
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupted = ""
    for line in data:
        status, res = check(line)
        if not status:
            corrupted += res
    return sum(score[c] for c in corrupted)


def cal(line):
    score = {")": 1, "]": 2, "}": 3, ">": 4}
    total = 0
    for c in line:
        total = total * 5 + score[c]
    return total


def part2(data):
    """Solve part 2."""
    score = []
    for line in data:
        status, res = check(line)
        if status:
            score.append(cal(res))
    score = sorted(score)
    return score[len(score) // 2]


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
