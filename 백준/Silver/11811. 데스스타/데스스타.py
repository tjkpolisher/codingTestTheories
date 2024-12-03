import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

a = [0] * N  # 음이 아닌 정수의 수열 a_i를 담은 리스트
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a[i] |= matrix[i][j]

print(*a)