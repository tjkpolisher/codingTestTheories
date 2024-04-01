from collections import deque

N, L = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
heights = deque(heights)
for _ in range(N):
    p = heights.popleft()
    if p > L:
        break
    L += 1
print(L)