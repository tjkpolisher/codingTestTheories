import sys
input = sys.stdin.readline

N = int(input())
space = [list(input().rstrip()) for _ in range(N)]


def bfs(x, y):
    q = [(x, y)]
    space[x][y] = '.'  # 이미 방문한 영역을 방문 처리(빈 공간으로 취급)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and space[nx][ny] == '*':
                space[nx][ny] = '.'
                q.append((nx, ny))


cnt = 0
for j in range(N):
    for k in range(N):
        if space[j][k] == '*':
            bfs(j, k)
            cnt += 1

print(cnt)