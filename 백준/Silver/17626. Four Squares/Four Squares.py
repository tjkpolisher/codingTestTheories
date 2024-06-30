import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    j = 1
    while j * j <= i:
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        else:
            dp[i] = dp[i - j * j] + 1
        j += 1
print(dp[-1])