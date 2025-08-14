import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
grid = []
crump = []
for i in range(R):
    line = list(input().rstrip())
    for j in range(C):
        if line[j] == '#':
            crump.append((i, j))
    grid.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
visited = set()


def bfs(a, b):
    global cnt
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visited.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if grid[nx][ny] == '#' and (nx, ny) not in visited:
                    q.append((nx, ny))
    cnt += 1


for c in crump:
    a, b = c
    if (a, b) not in visited:
        bfs(a, b)

print(cnt)