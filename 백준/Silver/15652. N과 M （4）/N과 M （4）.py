import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())


def sequence(n, s):
    if len(s) == M:
        print(*s)
        return
    for num in range(n, N + 1):
        sequence(num, s + [num])


ans = []
for i in range(1, N + 1):
    sequence(i, [i])