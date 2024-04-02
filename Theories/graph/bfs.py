# defaultdict: 키가 없을 때 기본값을 defaultdict 형태로 기본값을 지정
from collections import defaultdict, deque


def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    result = []
    bfs(start, adj_list, start, result)
    return result


def bfs(node, adj_list, start, result):
    visited = set()  # 방문할 노드를 저장할 집합

    queue = deque([start])
    visited.add(start)
    result.append(start)

    # 큐가 비어있지 않은 동안 반복
    while queue:
        node = queue.popleft()
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                # 인접한 노드를 방문 처리
                queue.append(neighbor)
                visited.add(neighbor)
                result.append(neighbor)


if __name__ == "__main__":
    ex1 = [[(1, 2), (1, 3), (2, 4), (2, 5),
            (3, 6), (3, 7), (4, 8), (5, 8),
            (6, 9), (7, 9)],
           1]
    ex2 = [[(0, 1), (1, 2), (2, 3), (3, 4),
            (4, 5), (5, 0)],
           1]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
