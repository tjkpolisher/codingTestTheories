import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
names = []
for _ in range(N):
    names.append(input().rstrip())

combs = combinations(names, 2)

ans = 0
for comb in combs:
    S, T = comb
    k = min(len(S), len(T))
    for i in range(1, k + 1):
        if S[:i] == T[-i:] or S[-i:] == T[:i]:
            ans += 1
            break

print(ans)