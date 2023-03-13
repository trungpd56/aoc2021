#!/usr/bin/env python3
from collections import defaultdict


def checkwin(board, nums):
    cols = zip(*board)
    for col in cols:
        if all(n in nums for n in col):
            return True
    for row in board:
        if all(n in nums for n in row):
            return True
    return False


def score(board, nums):
    return sum(n for row in board for n in row if n not in nums) * nums[-1]


with open('input.txt', 'r') as f:
    raw = f.read().strip().split('\n\n')

puz = list(map(int, raw[0].split(',')))
boards = defaultdict(list)
for i, board in enumerate(raw[1:]):
    for row in board.split('\n'):
        row = list(map(int, row.split()))
        boards[i].append(row)


done = False
first = True
nboard = [False] * len(boards)
for n in range(5, len(puz)):
    for i in boards:
        if checkwin(boards[i], puz[:n]):
            if first:
                part1 = score(boards[i], puz[:n])
                nboard[i] = True
                first = False
            else:
                nboard[i] = True
        if all(nboard):
            part2 = score(boards[i], puz[:n])
            done = True
            break
    if done:
        break


print(f'Part1: {part1}')
print(f'Part2: {part2}')
