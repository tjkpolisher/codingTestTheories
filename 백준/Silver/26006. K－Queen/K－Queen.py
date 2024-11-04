import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, C = map(int, input().split())
R -= 1
C -= 1

queens = []  # 흑색 퀸의 위치를 저장할 리스트
for _ in range(K):
    R_i, C_i = map(int, input().split())
    R_i -= 1
    C_i -= 1
    queens.append([R_i, C_i])

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]


def is_attacked_by_queen(R, C):
    for qr, qc in queens:
        # 같은 행
        if qr == R:
            return True
        # 같은 열
        if qc == C:
            return True
        # 같은 대각선상
        if abs(qr - R) == abs(qc - C):
            return True
    return False


is_check = is_attacked_by_queen(R, C)

is_escapable = False
for i in range(8):
    nx = R + dx[i]
    ny = C + dy[i]
    if 0 <= nx < N and 0 <= ny < N:
        if not is_attacked_by_queen(nx, ny):
            is_escapable = True
            break

# 최종 상태 판단
if is_check and not is_escapable:
    print("CHECKMATE")
elif is_check and is_escapable:
    print("CHECK")
elif not is_check and not is_escapable:
    print("STALEMATE")
else:
    print("NONE")