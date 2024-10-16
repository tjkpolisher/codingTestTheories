import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = []  # 도시 정보를 저장할 2차원 리스트
houses = []  # 집의 좌표를 저장할 리스트
chickens = []  # 치킨집의 좌표를 저장할 리스트
for i in range(N):
    row = list(map(int, input().split()))
    for j, building in enumerate(row):
        if building == 1:  # 집
            houses.append([i, j])
        elif building == 2:  # 치킨집
            chickens.append([i, j])
    city.append(row)

candidates = list(combinations(chickens, M))


def get_sum(candidate):
    result = 0
    for hx, hy in houses:
        temp = float('inf')
        for cx, cy in candidate:
            temp = min(temp, abs(cx - hx) + abs(cy - hy))
        result += temp
    return result


result = float('inf')
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)