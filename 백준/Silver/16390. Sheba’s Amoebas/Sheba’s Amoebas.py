import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(m)]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    # 이동 방향
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '#':
                grid[nx][ny] = '.'
                q.append((nx, ny))


cnt = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#':
            bfs(i, j)
            cnt += 1
print(cnt)