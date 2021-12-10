from lib import open_file


lines = open_file("input/day4.txt")

numbers = [int(e) for e in lines[0].split(",")]
data = []
grid = []
for line in lines[2:]:
    if line == "":
        data.append(grid)
        grid = []
    else:
        row = [int(e) for e in line.split()]
        grid.append(row)
if grid:
    data.append(grid)

# A marked row or columns is filled with -1
def check_grid(grid):
    for row in grid:
        if sum(row) == -5:
            return True
    for i in range(len(grid[0])):
        column_ok = True
        for row in grid:
            if row[i] != -1:
                column_ok = False
        if column_ok:
            return True

def part_1():
    grids = data
    for num in numbers:
        for grid in grids:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == num:
                        grid[i][j] = -1
            if check_grid(grid):
                res = 0
                for row in grid:
                    for elt in row:
                        if elt != -1:
                            res += elt
                return res *  num
    return -1

print(f"Part 1 answer {part_1()}")

def part_2():
    grids = data
    winning_grid = None
    winning_grids_idx = []
    for num in numbers:
        if len(winning_grids_idx) == len(grids):
            break
        for i in range(len(grids)):
            if i in winning_grids_idx:
                continue
            for j in range(len(grids[i])):
                for k in range(len(grids[i][j])):
                    if grids[i][j][k] == num:
                        grids[i][j][k] = -1
            if check_grid(grids[i]):
                winning_grid = (num, grids[i])
                winning_grids_idx.append(i)
    last_num, last_grid = winning_grid
    res = 0
    for row in last_grid:
        for elt in row:
            if elt != -1:
                res += elt
    return res *  last_num

print(f"Part 2 answer {part_2()}")
