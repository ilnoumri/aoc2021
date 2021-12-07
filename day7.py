from lib import open_file


positions = [int(elt) for elt in open_file("input/day7.txt")[0].split(",")]

def part_1():
    res = None
    for i in range(len(positions)):
        fuel = 0
        for j in range(len(positions)):
            if j != i:
                fuel += abs(positions[i] - positions[j])
        if not res or fuel < res:
            res = fuel
    return res

print(f"Part 1 {part_1()}")

def part_2():
    res = None
    for i in range(max(positions)):
        cost = 0
        for pos in positions:
            fuel = abs(pos - i)
            cost += fuel * (fuel+1) // 2
        if not res or cost < res:
            res = cost
    return res

print(f"Part 2 {part_2()}")

