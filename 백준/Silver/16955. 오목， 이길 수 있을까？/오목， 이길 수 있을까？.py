# 보드를 입력 받습니다.
board = []
for _ in range(10):
    board.append(list(input()))

# 방향 벡터 정의 (우, 하, 우하대각선, 우상대각선)
directions = [(0,1), (1,0), (1,1), (-1,1)]


def check_win(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'X':
                # 네 가지 방향에 대해 확인
                for dx, dy in directions:
                    cnt = 1
                    x, y = i, j
                    # 이전 위치가 보드 범위를 벗어나지 않고, 'X'라면 continue
                    prev_x, prev_y = x - dx, y - dy
                    if 0 <= prev_x < 10 and 0 <= prev_y < 10 and board[prev_x][prev_y] == 'X':
                        continue
                    x += dx
                    y += dy
                    while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == 'X':
                        cnt += 1
                        x += dx
                        y += dy
                    if cnt >= 5:
                        return True
    return False


for i in range(10):
    for j in range(10):
        if board[i][j] == '.':
            board[i][j] = 'X'
            if check_win(board):
                print(1)
                exit()
            board[i][j] = '.'

print(0)