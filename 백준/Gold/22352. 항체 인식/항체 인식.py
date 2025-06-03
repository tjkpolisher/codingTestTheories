import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

post = []
for _ in range(N):
    post.append(list(map(int, input().split())))

if grid == post:
    print("YES")
    exit()

start_r = start_c = None
for i in range(N):
    for j in range(M):
        if grid[i][j] != post[i][j]:
            start_r, start_c = i, j
            break
    if start_r is not None:
        break

orig_val = grid[start_r][start_c]
new_val = post[start_r][start_c]
orig_grid = [row[:] for row in grid]

visited = [[False] * M for _ in range(N)]
q = deque()
q.append((start_r, start_c))
visited[start_r][start_c] = True
component = [(start_r, start_c)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    r, c = q.popleft()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if orig_grid[nr][nc] == orig_val:
                visited[nr][nc] = True
                q.append((nr, nc))
                component.append((nr, nc))

for r, c in component:
    grid[r][c] = new_val

if grid == post:
    print("YES")
else:
    print("NO")