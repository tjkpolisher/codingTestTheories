N = int(input())
moves = list(input())

board = [['.'] * N for _ in range(N)]
dx = [-1, 1, 0, 0]  # U, D, L, R 순서
dy = [0, 0, -1, 1]
x, y = 0, 0  # 초기 위치


def carve(x, y, move):
    if board[x][y] == '.':
        if move in ('L', 'R'):
            board[x][y] = '-'
        if move in ('U', 'D'):
            board[x][y] = '|'
    if board[x][y] == '|':
        if move in ('L', 'R'):
            board[x][y] = '+'
    if board[x][y] == '-':
        if move in ('U', 'D'):
            board[x][y] = '+'


for move in moves:
    if move == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    if move == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    if move == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    if move == 'R':
        nx = x + dx[3]
        ny = y + dy[3]

    # 목판 바깥으로 나가는 명령일 경우 무시하고 다음 명령 진행
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    carve(x, y, move)
    carve(nx, ny, move)
    x, y = nx, ny

for row in board:
    print(''.join(row))