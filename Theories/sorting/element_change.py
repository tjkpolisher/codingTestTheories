import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    A[i], B[i] = B[i], A[i]

print(sum(A))
