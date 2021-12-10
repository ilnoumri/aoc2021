from lib import open_file


lines = open_file("input/day8.txt")

def part_1():
    res = 0
    for line in lines:
        for pattern in line.split("|")[1].strip().split():
            if len(pattern) in (2, 3, 4, 7):
                res += 1
    return res

print(f"Part 1 {part_1()}")

def part_2():
    res = 0
    return res
print(f"Part 2 {part_2()}")
