import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split())

monsters = []
equipments = []

for _ in range(N):
    a, x = map(int, input().split())
    if a == 1:
        heapq.heappush(monsters, x)
    else:
        heapq.heappush(equipments, x)

cnt = len(equipments)  # 장비 방은 전투력과 무관하게 무조건 돌파 가능하므로 장비 방의 개수로 초기화

while monsters:
    while equipments and monsters[0] >= D:
        D *= heapq.heappop(equipments)
    if monsters[0] < D:
        cnt += 1
        D += heapq.heappop(monsters)
    else:
        break

print(cnt)