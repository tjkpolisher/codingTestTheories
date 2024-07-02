T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]
    if N > 5:
        for i in range(5, N):
            dp.append(dp[i - 5] + dp[i - 1])
    print(dp[N - 1])