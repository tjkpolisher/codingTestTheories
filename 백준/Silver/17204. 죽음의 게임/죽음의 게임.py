from collections import deque

N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i].append(int(input()))


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        v = queue.popleft()
        if v == K:
            return count
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        count += 1

    return -1


visited = [False] * N
print(bfs(graph, 0, visited))