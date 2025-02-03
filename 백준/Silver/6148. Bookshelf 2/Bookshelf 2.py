import sys
input = sys.stdin.readline

N, B = map(int, input().split())
heights = []
sum_height = 0
for _ in range(N):
    height = int(input())
    heights.append(height)
    sum_height += height


def backtracking(start, total):
    if total >= B:
        global ans
        ans = min(ans, total - B)
        return
    for i in range(start, N):
        backtracking(i + 1, total + heights[i])


ans = 10 ** 9
backtracking(0, 0)

print(ans)