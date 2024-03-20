import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    ans = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                ans += 1
    return ans


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    visited = [False] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(graph, 1, visited))