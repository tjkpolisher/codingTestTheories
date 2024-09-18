import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color, visited, grid):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and grid[ny][nx] == color:
                    visited[ny][nx] = True
                    q.append((nx, ny))


visited_normal = [[False] * N for _ in range(N)]
count_normal = 0
for j in range(N):
    for i in range(N):
        if not visited_normal[j][i]:
            bfs(i, j, grid[j][i], visited_normal, grid)
            count_normal += 1

graph_rg = [row[:] for row in grid]  # 원본 그래프 복사
for j in range(N):
    for i in range(N):
        if graph_rg[j][i] == 'G':
            graph_rg[j][i] = 'R'

visited_rg = [[False] * N for _ in range(N)]
count_rg = 0

for j in range(N):
    for i in range(N):
        if not visited_rg[j][i]:
            bfs(i, j, graph_rg[j][i], visited_rg, graph_rg)
            count_rg += 1

print(count_normal, count_rg)