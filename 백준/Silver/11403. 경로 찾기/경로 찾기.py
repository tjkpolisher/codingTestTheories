import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(N)]


def bfs(start):
    q = deque()
    q.append(start)
    check = [0 for _ in range(N)]

    while q:
        v = q.popleft()
        for i in range(N):
            if not check[i] and graph[v][i]:
                q.append(i)
                check[i] = 1
                visited[start][i] = 1


for i in range(N):
    bfs(i)

for i in visited:
    print(*i)