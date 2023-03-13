#!/usr/bin/env python3

import sys
from collections import defaultdict


def decode(pattern):
    code = [[]] * 10
    for word in pattern.split():
        word = set(word)
        if len(word) == 2:
            code[1] = word
        elif len(word) == 4:
            code[4] = word
        elif len(word) == 3:
            code[7] = word
        elif len(word) == 7:
            code[8] = word

    for word in pattern.split():
        word = set(word)
        if len(word) == 6:
            if code[4].issubset(word):
                code[9] = word
            elif code[1].issubset(word):
                code[0] = word
            else:
                code[6] = word

    for word in pattern.split():
        word = set(word)
        if len(word) == 5:
            if code[7].issubset(word):
                code[3] = word
            elif word.issubset(code[9]) and not code[7].issubset(word):
                code[5] = word
            elif not code[7].issubset(word):
                code[2] = word

    return code


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

cnt = defaultdict(int)
num = 0
for line in lines:
    # be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    pattern, output = line.split(' | ')
    code = decode(pattern)
    digits = ""
    for word in output.split():
        word = set(word)
        cnt[code.index(word)] += 1
        digits += str(code.index(word))
    num += int(digits)


print(f'Part1: {sum(cnt.values())}')
print(f'Part2: {num}')
