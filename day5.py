from lib import open_file

lines = [line.replace(",", ".") for line in open_file("input/day5.txt")]

# Bresenhams line algorithm 
def get_points(x0, y0, x1, y1):
    dx = abs(x1-x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1-y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    res = []
    while True:
        res.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    return res

def part_1():
    covered_points = {}
    for line in lines:
        org, dst = line.split(" -> ")
        x1, y1 = [int(e) for e in org.split(".")]
        x2, y2 = [int(e) for e in dst.split(".")]
        if x1 == x2 or y1 == y2:
            points = get_points(x1, y1, x2, y2)
            for point in points:
                if point in covered_points.keys():
                    covered_points[point] += 1
                else:
                    covered_points[point] = 1
    res = 0
    for key in covered_points.keys():
        if covered_points[key] >= 2:
            res += 1
    return res

print(f"Part 1 answer {part_1()}")

def part_2():
    covered_points = {}
    for line in lines:
        org, dst = line.split(" -> ")
        x1, y1 = [int(e) for e in org.split(".")]
        x2, y2 = [int(e) for e in dst.split(".")]
        points = get_points(x1, y1, x2, y2)
        for point in points:
            if point in covered_points.keys():
                covered_points[point] += 1
            else:
                covered_points[point] = 1
    res = 0
    for key in covered_points.keys():
        if covered_points[key] >= 2:
            res += 1
    return res

print(f"Part 2 answer {part_2()}")
