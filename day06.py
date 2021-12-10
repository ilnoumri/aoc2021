from lib import open_file
fishes = [int(e) for e in open_file("input/day6.txt")[0].split(",")]

def rotate(l):
    return l[1:] + l[:1]

def simulate(days):
    groups = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(groups)):
      groups[i] = fishes.count(i)
    for _ in range(days):
        n0 = groups[0]
        groups = rotate(groups)
        groups[6] += n0
    return sum(groups)

def part_1():
    return simulate(80)

print(f"Part 1 answer {part_1()}")

def part_2():
    return simulate(256)

print(f"Part 2 answer {part_2()}")
