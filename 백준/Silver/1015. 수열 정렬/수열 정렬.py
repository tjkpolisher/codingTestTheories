import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)
P = []
for i in range(N):
    idx = A_sorted.index(A[i])
    P.append(idx)
    A_sorted[idx] = -1  # 이미 할당한 숫자를 -1로 대체해 재탐색되지 않도록 처리.

print(*P)