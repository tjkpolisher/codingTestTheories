from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 2)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, N + 2):
    graph[i] = sorted(graph[i])


def dfs(graph, start, visited):
    v = start
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

visited = [False] * (N + 1)
bfs(graph, V, visited)