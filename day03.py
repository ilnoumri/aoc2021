from lib import open_file


lines = open_file("input/day3.txt")

def part_1():
    gamma, epsilon = "", ""
    for i in range(len(lines[0])):
        n0, n1 = 0, 0
        for line in lines:
            if line[i] == "0":
                n0 += 1
            else:
                n1 += 1
        if n0 > n1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)

print(f"Part 1 answer {part_1()}")

def part_2():
    tmp_ocr, tmp_csr = lines, lines
    for i in range(len(tmp_ocr[0])):
        b0, b1 = [], []
        for line in tmp_ocr:
            if line[i] == "0":
                b0.append(line)
            else:
                b1.append(line)
        if len(b0) > len(b1):
            tmp_ocr = b0
        else:
            tmp_ocr = b1    
        if len(tmp_ocr) == 1:
            break
    for i in range(len(tmp_csr[0])):
        b0, b1 = [], []
        for line in tmp_csr:
            if line[i] == "0":
                b0.append(line)
            else:
                b1.append(line)
        if len(b0) <= len(b1):
            tmp_csr = b0
        else:
            tmp_csr = b1
        if len(tmp_csr) == 1:
            break
    ocr, csr = tmp_ocr[0], tmp_csr[0]
    return int(ocr, 2) * int(csr, 2)

print(f"Part 2 answer {part_2()}")
