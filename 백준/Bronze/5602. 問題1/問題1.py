import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {i: 0 for i in range(1, m + 1)}
for _ in range(n):
    result = list(map(int, input().split()))
    for j in range(m):
        d[j + 1] += result[j]

d_items = d.items()
d_items = sorted(d_items, reverse=True, key=lambda x: x[1])
for k in d_items:
    print(k[0], end=' ')