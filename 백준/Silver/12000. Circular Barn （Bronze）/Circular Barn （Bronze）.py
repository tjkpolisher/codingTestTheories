import sys
input = sys.stdin.readline

n = int(input())
cows = [int(input()) for _ in range(n)]
ans = 10 ** 9

for i in range(n):
    dist = 0
    for j in range(n):
        idx = (i + j) % n
        dist += cows[idx] * j
    ans = min(ans, dist)

print(ans)