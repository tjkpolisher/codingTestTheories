import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def count_components():
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] and not visited[i][j]:
                bfs(i, j, visited)
                cnt += 1

    return cnt


def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])


def melt():
    melt_list = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                sea = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == 0:
                            sea += 1
                melt_list[i][j] = sea

    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                grid[i][j] = max(grid[i][j] - melt_list[i][j], 0)


time = 0
while True:
    components = count_components()

    if components >= 2:
        print(time)
        break

    if not components:
        print(0)
        break

    melt()
    time += 1