from lib import open_file


lines = open_file("input/day13.txt")

points = []
instructions = []
i = 0
for i in range(len(lines)):
    if lines[i] != '':
        x, y = [int(elt) for elt in lines[i].split(",")]
        points.append((x, y))
    else:
        break
for j in range(i+1, len(lines)):
    instructions.append(lines[j])

def fold(points,x=0, y=0):
    base = set()
    if y:
        base = set([point for point in points if point[1] < y])
        to_fold = [point for point in points if point[1] > y]
        for elt in to_fold:
            new = (elt[0], y - (elt[1] - y))
            base.add(new)
    elif x:
        base = set([point for point in points if point[0] < x])
        to_fold = [point for point in points if point[0] > x]
        for elt in to_fold:
            new = (x - (elt[0] - x), elt[1])
            base.add(new)
    return base

def part_1():
    base = set(points)
    axis, nb = instructions[0].split()[-1].split("=")
    if axis == "x":
        base = fold(base, x=int(nb))
    elif axis == "y":
        base = fold(base, y=int(nb))
    return len(base)

print(f"Part 1 answer {part_1()}")

def part_2():
    base = set(points)
    for ins in instructions:
        axis, nb = ins.split()[-1].split("=")
        if axis == "x":
            base = fold(base, x=int(nb))
        elif axis == "y":
            base = fold(base, y=int(nb))
    res = []
    max_x, max_y = max(e[0] for e in base), max(e[1] for e in base)
    for y in range(max_y+1):
        dots = []
        for x in range(max_x+1):
            if (x,y) in base:
                dots.append('#')
            else:
                dots.append(".")
        res.append(dots)
    for elt in res:
        print(elt)

print(f"Part 2 answer")
part_2()
