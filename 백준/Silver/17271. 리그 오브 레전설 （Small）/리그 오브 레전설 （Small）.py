N, M = map(int, input().split())
MOD = 1000000007
if M > N:
    print(1)
    exit()

dp = [0] * (N + 1)

for i in range(1, M):
    dp[i] = 1
dp[M] = 2

for i in range(M + 1, N + 1):
    dp[i] = (dp[i - 1] + dp[i - M]) % MOD

print(dp[-1])