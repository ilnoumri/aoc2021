from lib import open_file
from collections import defaultdict

lines = open_file("input/day14.txt")

template = lines[0]
rules = {}
for i in range(2, len(lines)):
    k, v = lines[i].split(" -> ")
    rules[k] = v


def run(steps):
    temp = [template[i:i+2] for i in range(len(template)-1)]
    pairs = defaultdict(int)
    for pair in temp:
        pairs[pair] += 1
    count = defaultdict(int)
    for elt in template:
        count[elt] += 1
    for _ in range(steps):
        new_pairs = defaultdict(int)
        for k, v in pairs.items():
            inject = rules[k]
            new_pairs[k[0] + inject] += v
            new_pairs[inject + k[1]] += v
            count[inject] += v
        pairs = new_pairs
    return max(count.values()) - min(count.values())


def part_1():
    return run(10)    

print(f"Part 1 answer {part_1()}")

def part_2():
    return run(40)

print(f"Part 2 answer {part_2()}")
