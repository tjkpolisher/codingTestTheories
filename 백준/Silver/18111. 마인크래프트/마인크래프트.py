import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = []
for _ in range(N):
    h = list(map(int, input().split()))
    heights.append(h)

ans = int(1e9)
ground_level = 0

for i in range(257):
    used_block = 0
    taken_block = 0
    for x in range(N):
        for y in range(M):
            if heights[x][y] > i:
                used_block += heights[x][y] - i
            else:
                taken_block += i - heights[x][y]

    if used_block + B >= taken_block:
        if (used_block * 2) + taken_block <= ans:
            ans = (used_block * 2) + taken_block
            ground_level = i

print(ans, ground_level)