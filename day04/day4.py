#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    nums, *raws = puzzle_input.split("\n\n")
    nums = [int(n) for n in nums.split(",")]
    boards = []
    for raw in raws:
        boards.append([list(map(int, line.split())) for line in raw.splitlines()])
    return nums, boards


def is_win(board: list, nums: list):
    for row in board:
        if all(n in nums for n in row):
            return True
    cols = list(zip(*board))
    for col in cols:
        if all(n in nums for n in col):
            return True
    return False


def score(board: list, nums: list):
    return sum(n for row in board for n in row if n not in nums) * nums[-1]


def solution(data):
    """Solve part 1."""
    nums, boards = data
    done = [False] * len(boards)
    for i in range(len(nums)):
        for j, board in enumerate(boards):
            if is_win(board, nums[:i]):
                if True not in done:
                    part1 = score(board, nums[:i])
                done[j] = True
            if all(done):
                part2 = score(board, nums[:i])
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
