import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().rstrip().split()))

start = 0
end = max(heights)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for h in heights:
        if h > mid:
            total += h - mid

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)