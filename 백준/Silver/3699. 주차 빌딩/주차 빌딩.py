import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, l = map(int, input().split())  # 빌딩 높이, 컨베이어 벨트 길이
    t = 0  # 차를 찾는데 걸리는 총 시간
    heap = []

    for i in range(h):
        for j, car in enumerate(map(int, input().split())):
            if car == -1:
                continue
            heappush(heap, (car, i, j))

    conveyer_loc = {i: 0 for i in range(h)}  # 컨베이어 벨트의 위치(초기값 0)
    while heap:
        car, floor, loc = heappop(heap)
        t += (floor * 10 * 2 + min(abs(loc - conveyer_loc[floor]), l - abs(loc - conveyer_loc[floor])) * 5)
        conveyer_loc[floor] = loc
    print(t)