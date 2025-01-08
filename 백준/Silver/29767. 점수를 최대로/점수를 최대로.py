N, K = map(int, input().split())
classrooms = list(map(int, input().split()))

dp = [0] * N
dp[0] = classrooms[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + classrooms[i]

dp.sort(reverse=True)
print(sum(dp[:K]))