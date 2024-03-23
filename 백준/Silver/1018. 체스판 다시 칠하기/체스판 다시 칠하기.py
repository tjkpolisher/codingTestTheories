import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().strip())

minimum = 8 ** 2  # 칠해야 할 칸의 최소값(초기값은 8*8 영역을 다 칠하는 경우로 설정)

patterns = ['WBWBWBWB', 'BWBWBWBW'] * 4, ['BWBWBWBW', 'WBWBWBWB'] * 4

for i in range(N - 7):
    for j in range(M - 7):
        for pattern in patterns:
            cnt = 0
            for a in range(8):
                for b in range(8):
                    if board[i + a][j + b] != pattern[a][b]:
                        cnt += 1
            minimum = min(minimum, cnt)

print(minimum)