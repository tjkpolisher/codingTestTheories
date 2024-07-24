from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato_box = []
ripen = deque()  # 큐를 여기서 바로 선언하여 초기화

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            ripen.append((j, i))  # 모든 익은 토마토 위치 추가
    tomato_box.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    days = -1
    while ripen:
        for _ in range(len(ripen)):
            x, y = ripen.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = 1
                    ripen.append((nx, ny))
        days += 1

    # BFS 후에 토마토가 모두 익었는지 확인
    for row in tomato_box:
        if 0 in row:
            return -1
    return days

days = bfs()
print(days)
