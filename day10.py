from lib import open_file

lines = open_file("input/day10.txt")
matching = {"(": ")", "[": "]", "{": "}", "<": ">"}

def part_1():
    table = {")": 0, "]": 0, "}": 0, ">": 0}
    for line in lines:
        stack = []
        for elt in line:
            if elt in matching.keys():
                stack.append(elt)
            elif elt in matching.values():
                if matching[stack.pop()] != elt:
                    table[elt] += 1
                    break
    return table[")"] * 3 + table["]"] * 57 + table["}"] * 1197 + table[">"] * 25137

print(f"Part 1 answer {part_1()}")

def part_2():
    solutions = []
    for line in lines:
        stack = []
        for elt in line:
            if elt in matching.keys():
                stack.append(elt)
            elif elt in matching.values():
                if matching[stack.pop()] != elt:
                    stack = []
                    break
        if stack:
            rev = [matching[elt] for elt in reversed(stack)]
            solutions.append("".join(rev))
    res = []
    for solution in solutions:
        tmp = 0
        for elt in solution:
            tmp *= 5
            if elt == ')':
                tmp += 1 
            elif elt == ']':
                tmp += 2
            elif elt == '}':
                tmp += 3
            elif elt == '>':
                tmp += 4
        res.append(tmp)
    return sorted(res)[len(res)//2]

print(f"Part 2 answer {part_2()}")
        

