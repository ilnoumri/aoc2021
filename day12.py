from lib import open_file
from collections import defaultdict

lines = open_file("input/day12.txt")

visited = defaultdict(bool)

def build_graph():
    graph = defaultdict(list)
    for line in lines:
        org, dst = line.split("-")
        graph[org].append(dst)
        graph[dst].append(org)
    return graph

visited = defaultdict(int)

def dfs(graph, node, twice):
    if node == "end":
        return 1
    visited[node] += 1
    res = 0
    for adj in graph[node]:
        if adj.isupper() or not visited[adj]:
            res += dfs(graph, adj, twice)
        elif adj != "start" and twice and visited[adj]:
            res += dfs(graph, adj, False)
    visited[node] -= 1
    return res

graph = build_graph()
def part_1():
    return dfs(graph, "start", False)

print(f"Part 1 answer {part_1()}")

def part_2():
    return dfs(graph, "start", True)

print(f"Part 2 answer {part_2()}")
