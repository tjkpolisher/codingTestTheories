import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
heights = list(map(int, input().split()))

start = 0
end = max(heights)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for h in heights:
        if h > mid:
            total += h - mid

    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
    if total < M:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    else:
        result = mid
        start = mid + 1

print(result)
