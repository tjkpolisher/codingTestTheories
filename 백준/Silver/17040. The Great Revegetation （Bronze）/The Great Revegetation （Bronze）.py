import sys
input = sys.stdin.readline

N, M = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for a, b in connections:
    graph[a].append(b)
    graph[b].append(a)

result = [0] * (N + 1)
for pasture in range(1, N + 1):
    visited = {result[neighbor] for neighbor in graph[pasture]}

    for grass in range(1, 5):
        if grass not in visited:
            result[pasture] = grass
            break

print(''.join(map(str, result[1:])))