import sys
input = sys.stdin.readline

N = int(input())
w = list(map(int, input().split()))

d = [0] * 100
d[0] = w[0]
d[1] = max(w[0], w[1])
for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + w[i])

print(d[i])
