from lib import open_file


lines = open_file("input/day9.txt")


def get_low_points():
    low_points = []
    low_points_idx = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            up = (i, j-1)
            down = (i, j+1)
            left = (i-1, j)
            right = (i+1, j)
            directions = (up, down, left, right)
            to_add = True
            for direction in directions:
                x, y = direction
                if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
                    continue
                if lines[x][y] <= lines[i][j]:
                    to_add = False
            if to_add:
                low_points.append(int(lines[i][j]))
                low_points_idx.append((i, j))
    return low_points, low_points_idx

def part_1():
    low_points, _ = get_low_points()
    return sum(low_points) + len(low_points)

print(f"Part 1 answer {part_1()}")

seen = set()
def get_bassin(idx):
    i, j = idx
    bassin = []
    up = (i, j-1)
    down = (i, j+1)
    left = (i-1, j)
    right = (i+1, j)
    directions = (up, down, left, right)
    for direction in directions:
        x, y = direction
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
            continue
        adj = int(lines[x][y])
        if adj < 9:
            bassin.append(adj)
            adj_bassin = get_bassin((x, y))
            for elt in adj_bassin:
                bassin.append(elt)
    return bassin
       
def part_2():
    _, low_points_idx = get_low_points()
    bassins = []
    for idx in low_points_idx:
        bassin = get_bassin(idx)
        bassins.append(bassin)
    bassins = [len(bassin) for bassin in bassins]
    from math import prod
    return prod(sorted(bassins)[-3:])

print(f"Part 2 answer {part_2()}")
