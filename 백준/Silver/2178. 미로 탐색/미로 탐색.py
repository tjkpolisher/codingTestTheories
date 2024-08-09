import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze_line = list(input().rstrip())
    maze.append(maze_line)


def bfs(start):
    q = deque()
    q.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    while q:
        cnt += 1
        length = len(q)
        for _ in range(length):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if maze[ny][nx] == '0':
                    continue
                if maze[ny][nx] == '1':
                    q.append((nx, ny))
                    maze[ny][nx] = 0
                if ny == N - 1 and nx == M - 1:
                    return cnt
    return cnt


print(bfs((0, 0)))