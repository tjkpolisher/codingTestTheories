import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = []  # 숫자를 담을 직사각형 리스트

for _ in range(N):
    rectangle.append(list(input().rstrip()))


def answer(s):
    for i in range(N - s + 1):  # 행 인덱스
        for j in range(M - s + 1):  # 열 인덱스
            pivot = rectangle[i][j]
            key = (pivot == rectangle[i][j + s - 1]
                   and pivot == rectangle[i + s - 1][j]
                   and pivot == rectangle[i + s - 1][j + s - 1])
            if key:
                return True
    return False


size = min(N, M)
for k in range(size, 0, -1):
    if answer(k):
        print(k ** 2)
        break