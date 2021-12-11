from lib import open_file
from copy import deepcopy
lines = [list(int(e) for e in elt) for elt in open_file("input/day11.txt")]
reset = deepcopy(lines)

def get_adj(i, j):
    top = (i, j-1)
    bottom = (i, j+1)
    left = (i-1, j)
    right = (i+1, j)
    rtop = (i+1, j-1)
    rbottom = (i+1, j+1)
    ltop = (i-1, j-1)
    lbottom = (i-1, j+1)
    directions = (top, bottom, left, right, rtop, rbottom, ltop, lbottom)
    res = []
    for direction in directions:
        x, y = direction
        if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
            continue
        res.append(direction)
    return res

def part_1():
    flashed = 0
    seen = []
    for step in range(100):
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                lines[i][j] += 1
                if lines[i][j] > 9:
                    lines[i][j] = 0
                    seen.append((i, j))
        while seen:
            i, j = seen.pop(0)
            flashed += 1
            for (x,y) in get_adj(i, j):
                if lines[x][y] == 0:
                    continue
                lines[x][y] += 1
                if lines[x][y] > 9:
                    lines[x][y] = 0
                    seen.append((x, y))
    return flashed

print(f"Part 1 answer {part_1()}")

lines = reset

def part_2():
    seen = []
    step = 0
    while True:
        step += 1
        flashed = 0
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                lines[i][j] += 1
                if lines[i][j] > 9:
                    lines[i][j] = 0
                    seen.append((i, j))
        while seen:
            i, j = seen.pop(0)
            flashed += 1
            for (x,y) in get_adj(i, j):
                if lines[x][y] == 0:
                    continue
                lines[x][y] += 1
                if lines[x][y] > 9:
                    lines[x][y] = 0
                    seen.append((x, y))
        if flashed == (len(lines) * len(lines[0])):
            return step

print(f"Part 2 answer {part_2()}")
