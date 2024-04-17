import sys
input = sys.stdin.readline

N = int(input())
health = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))

# 체력 0부터 100까지, N명의 사람
dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):  # 사람의 수
    for j in range(101):  # 체력을 늘려가면서, dp에 들어갈 수 있는지 체크
        if health[i] <= j:  # 현재 체력이 현재 사람을 만나서 잃을 체력보다 많을 때
            # 이전 최대 체력과 비교해서 더 높은 체력을 dp에 입력
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - health[i]] + happiness[i])
        else:  # 체력이 없으면
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])