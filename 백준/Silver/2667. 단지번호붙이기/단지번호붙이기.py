import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
house = []
for i in range(N):
    line_string = input().rstrip()
    line = []
    for j in range(N):
        line.append(int(line_string[j]))
    house.append(line)


def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    q = deque()
    q.append(start)
    y_start, x_start = start[0], start[1]
    house[y_start][x_start] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if house[ny][nx] == 1:
                q.append((ny, nx))
                house[ny][nx] = 0
                cnt += 1
    return cnt


house_per_groups = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            house_per_groups.append(bfs((i, j)))

print(len(house_per_groups))
for counts in sorted(house_per_groups):
    print(counts)