from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 'X':
                continue
            if graph[ny][nx] == 'P' or graph[ny][nx] == 'O':
                if graph[ny][nx] == 'P':
                    cnt += 1
                graph[ny][nx] = 'X'
                q.append((nx, ny))
    return cnt


N, M = map(int, input().split())
graph = []
for i in range(N):
    info = input().rstrip()
    if 'I' in info:
        ix = info.index('I')
        iy = i
    graph.append(list(info))

ans = bfs(ix, iy)
if not ans:
    ans = 'TT'
print(ans)