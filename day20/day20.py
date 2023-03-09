#!/usr/bin/env python3


def enhanced(g, light=False):
    g2 = set()
    rvals = [p[0] for p in g]
    cvals = [p[1] for p in g]
    minr, maxr = min(rvals), max(rvals)
    minc, maxc = min(cvals), max(cvals)
    for r in range(minr-2, maxr+3):
        for c in range(minc-2, maxc+3):
            binstr = ""
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not light:
                        binstr += '1' if (r+dr, c+dc) in g else '0'
                    else:
                        binstr += '0' if (r+dr, c+dc) in g else '1'
            if light and algo[int(binstr, 2)] == '#':
                g2.add((r, c))
            elif not light and algo[int(binstr, 2)] == '.':
                g2.add((r, c))
    return g2


def pgrid(g):
    rvals = [p[0] for p in g]
    cvals = [p[1] for p in g]
    minr, maxr = min(rvals), max(rvals)
    minc, maxc = min(cvals), max(cvals)
    for r in range(minr-2, maxr+3):
        for c in range(minc-2, maxc+3):
            if (r, c) in g:
                print('#', end='')
            else:
                print('.', end='')
        print()


with open('input.txt', 'r') as f:
    algo, img = f.read().strip().split('\n\n')

img = img.split('\n')
g = set()
for r, line in enumerate(img):
    for c, char in enumerate(line.strip()):
        if char == '#':
            g.add((r, c))


for t in range(50):
    if t == 2:
        part1 = len(g)
    g = enhanced(g, t % 2)

print(f'Part1: {part1}')
part2 = len(g)
print(f'Part2: {part2}')
