import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)


def dfs(graph, node, visited):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)