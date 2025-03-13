import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * N
dp[0] = meetings[0][2]

for i in range(1, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + meetings[i][2])

print(dp[-1])