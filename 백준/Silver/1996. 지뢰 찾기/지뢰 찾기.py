import sys
input = sys.stdin.readline

N = int(input())
mine_map = []
ans = [[0] * N for _ in range(N)]
for i in range(N):
    row = input().rstrip()
    for j in range(N):
        if row[j] != '.':
            ans[i][j] = '*'
    mine_map.append(list(row))

# 탐색할 8개의 방향 지정(좌상, 상, 우상, 좌, 우, 좌하, 하, 우하)
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]
for i in range(N):
    for j in range(N):
        if ans[i][j] == '*':
            continue
        cnt = 0  # 지뢰의 개수
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if mine_map[nx][ny] != '.':
                cnt += int(mine_map[nx][ny])
            if cnt >= 10:
                ans[i][j] = 'M'
                break
        else:
            ans[i][j] = str(cnt)

# 출력
for i in range(N):
    print(''.join(ans[i]))