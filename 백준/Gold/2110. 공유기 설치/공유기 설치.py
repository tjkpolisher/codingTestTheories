import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

start = 1  # 최소 거리
end = houses[-1] - houses[0]  # 최대 거리
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= value + mid:
            value = houses[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)