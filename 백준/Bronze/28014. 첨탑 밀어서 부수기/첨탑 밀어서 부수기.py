N = int(input())
heights = list(map(int, input().split()))
cnt = 1
for i, h in enumerate(heights):
    if i > 0 and h >= heights[i-1]:
        cnt += 1
print(cnt)