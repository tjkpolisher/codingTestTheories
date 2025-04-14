import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_queen, *queens = map(int, input().split())
n_knight, *knights = map(int, input().split())
n_pawn, *pawns = map(int, input().split())

# 현재 이동 가능한 칸의 수
cnt = n * m - n_queen - n_knight - n_pawn

# 체스판 초기화
board = [[0 for _ in range(m)] for _ in range(n)]
# 폰, 퀸, 나이트가 있는 칸은 별도로 장애물 표시
for i in range(n_pawn):
    x, y = pawns[2 * i] - 1, pawns[2 * i + 1] - 1
    board[x][y] = "P"
for i in range(n_queen):
    x, y = queens[2 * i] - 1, queens[2 * i + 1] - 1
    board[x][y] = "Q"
for i in range(n_knight):
    x, y = knights[2 * i] - 1, knights[2 * i + 1] - 1
    board[x][y] = "K"

# 퀸이 이동 가능한 칸
q_xd = [0, -1, -1, -1, 0, 1, 1, 1]
q_yd = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(n_queen):
    x, y = queens[2 * i] - 1, queens[2 * i + 1] - 1
    for j in range(8):
        nx, ny = x + q_xd[j], y + q_yd[j]
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] in (0, 1):
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt -= 1
            nx += q_xd[j]
            ny += q_yd[j]

# 나이트가 이동 가능한 칸
k_xd = [-1, -2, -2, -1, 1, 2, 2, 1]
k_yd = [-2, -1, 1, 2, 2, 1, -1, -2]
for i in range(n_knight):
    x, y = knights[2 * i] - 1, knights[2 * i + 1] - 1
    for j in range(8):
        nx, ny = x + k_xd[j], y + k_yd[j]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in (0, 1):
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt -= 1

print(cnt)