import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    score = int(input())
    stairs[i] = score

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])