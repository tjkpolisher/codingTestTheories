def solution(graph, source):
    # 노드의 개수
    n = len(graph)
    # 거리 배열 초기화
    distance = [float("inf")] * n
    distance[source] = 0
    # 직전 경로 배열 초기화
    predecessor = [None] * n

    # 간선 수만큼 반복하여 최단 경로 갱신
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                # u를 거쳐서 v로 가는 경로의 거리가 기존 거리보다 짧은 경우
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight  # 최단 거리 갱신
                    predecessor[v] = u  # 직전 노드 업데이트

    # 음의 가중치 순회 체크
    for u in range(n):
        for v, weight in graph[u]:
            # u를 거쳐서 v로 가는 경로의 거리가 기존 거리보다 짧은 경우
            # 음의 가중치 순회가 발견된 것이므로 [-1]을 리턴
            if distance[u] + weight < distance[v]:
                return [-1]

    return [distance, predecessor]


if __name__ == "__main__":
    ex1 = [[[(1, 4), (2, 3), (4, -6)],
            [(3, 5)],
            [(1, 2)],
            [(0, 7), (2, 4)],
            [(2, 2)]],
           0]
    ex2 = [[[(1, 5), (2, -1)],
            [(2, 2)],
            [(3, -2)],
            [(0, 2), (1, 6)]],
           0]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
