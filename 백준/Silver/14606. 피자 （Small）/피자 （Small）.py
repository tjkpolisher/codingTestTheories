N = int(input())


def divide(N):
    dp = [0, 0, 1]  # 피자판이 0개 1개, 2개, ..., n개일 때의 기쁨 정도
    for i in range(3, N + 1):
        dp.append(i - 1 + dp[i - 1])
    return dp[N]


print(divide(N))