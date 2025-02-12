import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

dp = [[0 for _ in range(7)] for _ in range(10 ** 6 + 1)]  # 높이별로 가능한 트리의 모양 개수를 저장할 dp 테이블
dp[0] = [1, 1, 1, 1, 1, 1, 1]  # 높이 1인 트리는 나올 수 있는 경우의 수가 하나 뿐이고, 암묵적으로 모든 경우의 수를 1로 지정
dp[1] = [1, 1, 1, 2, 2, 2, 3]  # 높이 2인 트리의 경우의 수

# 점화식 계산
for i in range(2, 10 ** 6 + 1):
    dp[i][0] = dp[i - 1][0] % MOD
    dp[i][1] = dp[i - 1][1] % MOD
    dp[i][2] = dp[i - 1][2] % MOD
    dp[i][3] = (dp[i - 2][3] * dp[i - 1][3] + dp[i - 1][3] * dp[i - 1][3]) % MOD
    dp[i][4] = (dp[i - 2][4] * dp[i - 1][4] + dp[i - 1][4] * dp[i - 2][4]) % MOD
    dp[i][5] = (dp[i - 2][5] * dp[i - 1][5] + dp[i - 1][5] * dp[i - 1][5]) % MOD
    dp[i][6] = (dp[i - 2][6] * dp[i - 1][6] + dp[i - 1][6] * dp[i - 1][6] + dp[i - 1][6] * dp[i - 2][6]) % MOD

T = int(input())
for _ in range(T):
    h, S_norm = map(int, input().split())
    h -= 1
    S = input().rstrip()

    if S == '-1':
        print(dp[h][0])
    elif S == '0':
        print(dp[h][1])
    elif S == '1':
        print(dp[h][2])
    elif S == '-1 0':
        print(dp[h][3])
    elif S == '-1 1':
        print(dp[h][4])
    elif S == '0 1':
        print(dp[h][5])
    else:
        print(dp[h][6])