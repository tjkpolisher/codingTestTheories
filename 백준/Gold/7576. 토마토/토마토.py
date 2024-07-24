from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato_box = []
ripen = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            ripen.append((j, i))
    tomato_box.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(ripen):
    q = deque(ripen)
    cnt = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = 1
                    q.append((nx, ny))
        cnt += 1
    return cnt


cnt = bfs(ripen)
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            cnt = -1
print(cnt)