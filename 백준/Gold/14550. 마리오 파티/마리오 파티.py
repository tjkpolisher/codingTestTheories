import sys
input = sys.stdin.readline

while True:
    test_case = input().rstrip()
    if test_case == '0':
        break

    N, S, T = test_case.split()  # 출발점과 별 사이의 칸수, 주사위의 눈 범위, 최대 턴
    N, S, T = int(N), int(S), int(T)
    board = []
    while len(board) < N:
        board.extend(map(int, input().split()))

    dp = [[False] * N for _ in range(T)]
    for i in range(S):
        dp[0][i] = board[i]

    for i in range(1, T - 1):
        for j in range(N):
            tmp = -(10 ** 10)
            if j == 0:
                tmp = 0
            for k in range(1, S + 1):
                if 0 <= j - k < N:
                    if not dp[i - 1][j - k]:
                        continue
                    tmp = max(tmp, dp[i - 1][j - k])

            dp[i][j] = tmp + board[j]

    ans = -10 ** 10
    for i in range(1, S + 1):
        ans = max(ans, dp[-2][-i])
    print(ans)