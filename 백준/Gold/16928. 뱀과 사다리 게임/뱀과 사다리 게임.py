from collections import deque

N, M = map(int, input().split())
graph = [i for i in range(101)]

# 사다리의 정보를 그래프에 추가
for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y
# 뱀의 정보를 그래프에 추가
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v


def bfs(start):
    q = deque()
    q.append(start)
    dist = [-1] * 101
    dist[1] = 0

    while q:
        v = q.popleft()
        if v == 100:
            return dist[100]
        for dice in range(1, 7):
            next_v = v + dice
            if next_v > 100:
                continue  # 결과가 100을 넘으면 다음 위치로 스킵

            final_v = graph[next_v]
            if dist[final_v] == -1:
                dist[final_v] = dist[v] + 1
                q.append(final_v)
    return -1  # 100번 칸에 도달할 수 없으면 -1을 리턴


print(bfs(1))