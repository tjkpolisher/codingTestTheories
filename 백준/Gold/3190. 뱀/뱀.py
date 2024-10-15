N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]  # 게임이 진행되는 보드
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())
snake_movements = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    snake_movements.append((X, C))


def turn(direction, C):
    if C == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


cnt = 0  # 게임 진행 시간
x, y = 0, 0   # 뱀의 첫 위치

# 방향 정보: 초기조건은 오른쪽을 보고 있음(리스트 상에는 시계 방향으로 돌아가며 배치)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board[x][y] = -1
direction = 0  # 초기 방향
idx = 0  # 다음에 회전할 정보
snake_current = [(x, y)]

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != -1:
        # 사과가 없을 경우 - 이동 후, 꼬리 제거
        if board[nx][ny] == 0:
            board[nx][ny] = -1
            snake_current.append((nx, ny))
            tx, ty = snake_current.pop(0)
            board[tx][ty] = 0
        # 사과가 있을 경우 - 이동 후 꼬리 그대로 두기
        if board[nx][ny] == 1:
            board[nx][ny] = -1
            snake_current.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪힐 경우
    else:
        cnt += 1
        break

    x, y = nx, ny  # 위치 갱신
    cnt += 1
    # 회전할 시간이 되면 회전
    if idx < L and cnt == snake_movements[idx][0]:
        direction = turn(direction, snake_movements[idx][1])
        idx += 1

print(cnt)