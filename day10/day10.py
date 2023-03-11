#!/usr/bin/env python3

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '<': '>',
    '(': ')',
    '{': '}',
    '[': ']',
}

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def cal(*args):
    result = 0
    prev = 0
    for i in range(len(args)):
        result = score2[args[i]] + prev * 5
        prev = result
    return result


with open('input.txt', 'r') as f:
    lines = f.readlines()

il = []
fi = []
for line in lines:
    pairs = []
    corrupt = False
    for c in line.strip():
        if c in '([{<':
            pairs.append(c)
        elif c in ')]}>':
            if match[c] != pairs.pop():
                il.append(c)
                corrupt = True
                break
    if not corrupt:
        fi.append([match[c] for c in pairs[::-1]])


part1 = sum(score[i] for i in il)
print(f'Part1: {part1}')

part2 = sorted([cal(*i) for i in fi])[len(fi)//2]
print(f'Part2: {part2}')
