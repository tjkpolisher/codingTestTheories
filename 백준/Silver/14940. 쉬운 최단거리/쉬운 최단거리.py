import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map_array = []
for i in range(n):
    line = list(map(int, input().split()))
    if 2 in line:
        y = i
        x = line.index(2)
    map_array.append(line)

# print(f"{x=}, {y=}")
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
map2 = [[-1] * m for _ in range(n)]
map2[y][x] = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= n or nx >= m:
                continue
            if map_array[ny][nx] == 0:
                map2[ny][nx] = 0
            if map_array[ny][nx] == 1 and map2[ny][nx] == -1:
                map2[ny][nx] = map2[y][x] + 1
                q.append((nx, ny))


bfs(x, y)
for i in range(n):
    for j in range(m):
        if map_array[i][j] == 0:
            map2[i][j] = 0

for i in range(n):
    print(*map2[i])