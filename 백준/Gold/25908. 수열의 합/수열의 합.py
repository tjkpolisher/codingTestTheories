S, T = map(int, input().split())


def summation(n):
    ans = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            ans += n // i
        else:
            ans -= n // i
    return ans


print(summation(T) - summation(S - 1))