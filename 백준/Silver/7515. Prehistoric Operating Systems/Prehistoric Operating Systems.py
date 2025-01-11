import sys
input = sys.stdin.readline


def calculate(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    dp = [0] * (n + 1)
    dp[1], dp[2] = 2, 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


T = int(input())
for i in range(T):
    n = int(input())

    print(f"Scenario {i + 1}:\n{calculate(n)}")
    if i != T - 1:
        print()