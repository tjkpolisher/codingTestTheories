from collections import deque


def bfs(start, result, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                result[i] = result[v] + 1
                visited[i] = True


n = int(input())
a1, a2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(a1, result, visited)
print(result[a2] if result[a2] > 0 else -1)