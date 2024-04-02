N = int(input())
S = input()

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in range(1, 4):
        if i - j >= 0:
            num = int(S[i - j:i])
            if S[i - j] != '0' and num > 0 and num <= 641:
                dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[N])