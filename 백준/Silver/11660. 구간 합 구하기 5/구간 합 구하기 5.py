import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0] for _ in range(N + 1)]
grid[0] = [0] * (N + 1)
for i in range(1, N + 1):
    grid[i].extend(list(map(int, input().split())))

prefix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for y in range(N):
    for x in range(N):
        prefix[x + 1][y + 1] = prefix[x][y + 1] + prefix[x + 1][y] - prefix[x][y] + grid[x + 1][y + 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(ans)