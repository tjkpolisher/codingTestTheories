N, M = map(int, input().split())
picture = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1 - 1, y2):
        for i in range(x1 - 1, x2):
            picture[j][i] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if picture[j][i] > M:
            ans += 1

print(ans)
