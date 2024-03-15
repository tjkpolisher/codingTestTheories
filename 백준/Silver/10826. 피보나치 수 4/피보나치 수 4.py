n = int(input())

dp = [0] * 10001  # n은 10,000 이하의 자연수 또는 0
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])