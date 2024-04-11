# 문제 출처: Summer/Winter Coding(~2018) - 배달
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq


def solution(N, road, K):
    """solution

    Args:
        N (integer): 마을의 개수
        road (iterable): 각 마을을 연결하는 도로의 정보
                        (각각 시작점, 끝점, 두 마을 사이의 거리를 뜻함)
        K (integer): 음식 배달이 가능한 시간

    Returns:
        integer: 음식 주문을 받을 수 있는 마을의 개수
    """
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


if __name__ == '__main__':
    ex1 = [5,
           [[1, 2, 1], [2, 3, 3], [5, 2, 2],
            [1, 4, 2], [5, 3, 1], [5, 4, 2]],
           3]
    ex2 = [6,
           [[1, 2, 1], [1, 3, 2], [2, 3, 2],
            [3, 4, 3], [3, 5, 2], [3, 5, 3],
            [5, 6, 1]],
           4]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1], e[2]))
