import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
visited = [False] * (N + 1)


def bfs(n):
    counter = 0
    q = deque()
    q.append(n)
    visited[n] = True

    while q:
        x = q.popleft()
        counter += 1

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return counter


for i in range(1, N + 1):
    if not visited[i]:
        cnt *= bfs(i)

print(cnt % 1000000007)