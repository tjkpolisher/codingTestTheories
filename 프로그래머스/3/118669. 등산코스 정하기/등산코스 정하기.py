def solution(n, paths, gates, summits):
    import heapq

    INF = 10 ** 9
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        i, j, w = path[0], path[1], path[2]
        graph[i].append((j, w))
        graph[j].append((i, w))

    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    distance = [INF] * (n + 1)
    q = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, (0, gate))

    while q:
        d, i = heapq.heappop(q)
        if distance[i] < d or is_summit[i]:
            continue

        for j, intensity in graph[i]:
            intensity = max(intensity, distance[i])
            if distance[j] > intensity:
                distance[j] = intensity
                heapq.heappush(q, (intensity, j))

    answer = [-1, INF]
    summits.sort()
    for summit in summits:
        d_summit = distance[summit]
        if d_summit < answer[1]:
            answer[0] = summit
            answer[1] = d_summit

    return answer