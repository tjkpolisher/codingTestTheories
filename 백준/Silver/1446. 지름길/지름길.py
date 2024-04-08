import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]

# 지름길 정보 입력
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:  # 역주행이 불가능하므로 도착점이 D보다 크면 제외
        continue
    graph[a].append((b, c))  # 모든 지름길은 일방통행이므로 단방향 간선

# 거리를 무한대로 초기화
distance = [INF] * (D + 1)
# 지름길이 없는 노드들은 전부 거리 1로 초기화
for i in range(D):
    graph[i].append((i + 1, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작점 거리를 0으로 초기화
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            d_temp = d + i[1]
            if d_temp < distance[i[0]]:
                distance[i[0]] = d_temp
                heapq.heappush(q, (d_temp, i[0]))


# 시작점 거리가 0이므로 0에서 출발하는 걸로 설정
dijkstra(0)
print(distance[D])