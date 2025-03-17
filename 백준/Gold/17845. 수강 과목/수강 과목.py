import sys
input = sys.stdin.readline

N, K = map(int, input().split())
subjects = [list(map(int, input().split())) for _ in range(K)]
subjects.insert(0, [0, 0])

dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(K + 1):
    I, T = subjects[i]  # 중요도, 공부 시간
    for j in range(N + 1):
        if T > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - T] + I, dp[i - 1][j])

print(dp[K][N])