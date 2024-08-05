import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
num = [0] * 10


def number(start, end, N, max_num, fruit):
    if end >= N:
        return max_num

    num[S[end]] += 1
    if num[S[end]] == 1:
        fruit += 1

    if fruit > 2:
        num[S[start]] -= 1
        if num[S[start]] == 0:
            fruit -= 1
        start += 1

    max_num = max(max_num, end - start + 1)
    return number(start, end + 1, N, max_num, fruit)


print(number(0, 0, N, 0, 0))