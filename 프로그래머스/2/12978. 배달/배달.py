import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distances = [float("inf")] * (N + 1)
    distances[1] = 0

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, node = heapq.heappop(q)
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    answer = 0
    for d in distances:
        if d <= K:
            answer += 1
    return answer