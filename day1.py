from lib import open_file


lines = [int(line) for line in open_file("input/day1.txt")]

def part_1():
    old = lines[0]
    res = 0
    for i in range(1, len(lines)):
        cur = lines[i]
        if cur > old:
            res += 1
        old = cur
    return res

print(f"Part 1 answer {part_1()}")

def part_2():
    res = 0
    old = lines[:3]
    for i in range(1, len(lines)):
        if (i+3) > len(lines):
            break
        cur = lines[i:i+3]
        if sum(cur) > sum(old):
            res += 1
        old = cur
    return res

print(f"Part 2 answer {part_2()}")

