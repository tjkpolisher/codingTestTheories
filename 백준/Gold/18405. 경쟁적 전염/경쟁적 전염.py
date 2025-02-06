from collections import deque

N, K = map(int, input().split())
cylinder = []
virus_location = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v:
            virus_location.append((v, i, j))
    cylinder.append(row)

virus_location.sort()  # 바이러스 번호의 오름차순으로 정렬

S, X, Y = map(int, input().split())
# 인덱싱 효율을 위해 X, Y에서 1씩 빼기
X -= 1
Y -= 1


def bfs(arr, S):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sec = 0
    q = deque(arr)
    while q:
        if sec == S:
            break
        for _ in range(len(q)):
            v, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if cylinder[nx][ny] == 0:
                    cylinder[nx][ny] = v
                    q.append((v, nx, ny))
        sec += 1


bfs(virus_location, S)
print(cylinder[X][Y])