from lib import open_file
from collections import defaultdict

lines = open_file("input/day15.txt")
graph = []

for line in lines:
    costs = [int(e) for e in line]
    graph.append(costs)

def get_adj(graph, loc):
    i, j = loc
    top = (i, j-1)
    bottom = (i, j+1)
    left = (i-1, j)
    right = (i+1, j)
    directions = (top, bottom, left, right)
    res = []
    for direction in directions:
        x, y = direction
        if x < 0 or x >= len(graph[0]) or y < 0 or y >= len(graph):
            continue
        res.append(direction)
    return res

def dijkstra(graph, org):
    q = []
    q.append(org)
    dist = defaultdict(int)
    dist[org] = 0
    while q:
        current = q.pop(0)
        for adj in get_adj(graph, current):
            x, y = adj
            new_dist = dist[current] + graph[x][y]
            if adj not in dist or dist[adj] > new_dist:
                dist[adj] = new_dist
                q.append(adj)
    return dist

def expand(graph):
    expanded = []
    for i in range(5):
        for y in range(len(graph)):
            row = []
            for j in range(5):
                for x in range(len(graph[0])):
                    val = graph[y][x] + i + j
                    if val > 9:
                        val -= 9
                    row.append(val)
            expanded.append(row)
    return expanded

def part_1():
    org, dst = (0,0), (len(graph[0])-1, len(graph)-1)
    cost = dijkstra(graph, org)
    return cost[dst]

print(f"Part 1 answer {part_1()}")

def part_2():
    expanded = expand(graph)
    org, dst = (0,0), (len(expanded[0])-1, len(expanded)-1)
    cost = dijkstra(expanded, org)
    return cost[dst]

print(f"Part 2 answer {part_2()}")
