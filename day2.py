from lib import open_file


lines = open_file("input/day2.txt")

def part_1():
    h, d = 0, 0
    for line in lines:
        cmd, value = line.split()
        if cmd == "forward":
            h += int(value)
        elif cmd == "down":
            d += int(value)
        elif cmd == "up":
            d -= int(value)
    return h * d

print(f"Part 1 answer {part_1()}")

def part_2():
    h, d, a = 0, 0, 0
    for line in lines:
        cmd, value = line.split()
        if cmd == "forward":
            h += int(value)
            d += a * int(value)
        elif cmd == "down":
            a += int(value)
        elif cmd == "up":
            a -= int(value)
    return h * d


print(f"Part 2 answer {part_2()}")
