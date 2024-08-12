import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
q = deque()
for i in range(H):
    layer = []
    for j in range(N):
        row = list(map(int, input().rstrip().split()))
        for k in range(M):
            if row[k] == 1:
                q.append((i, j, k))
        layer.append(row)
    graph.append(layer)


def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))


bfs()

max_days = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                sys.exit(0)
            max_days = max(max_days, graph[i][j][k])
print(max_days - 1)