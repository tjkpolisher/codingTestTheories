from collections import deque


def solution(info, edges):
    # 문제 출처: 2022 KAKAO BLIND RECRUITMENT - 양과 늑대
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/92343
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])

    max_sheep = 0
    q = deque([(0, 1, 0, set())])  # 시작점

    while q:
        current, sheep_cnt, wolf_cnt, visited = q.popleft()
        max_sheep = max(max_sheep, sheep_cnt)
        visited.update(tree[current])

        for next_node in visited:
            if info[next_node]:
                if sheep_cnt != wolf_cnt + 1:
                    q.append(
                        (next_node, sheep_cnt, wolf_cnt + 1, visited - {next_node})
                    )
            else:
                q.append(
                    (next_node, sheep_cnt + 1, wolf_cnt, visited - {next_node})
                )

    return max_sheep


if __name__ == "__main__":
    # 0은 양, 1은 늑대를 의미
    # info[0], 즉 루트 노드(0번 노드)는 항상 0(양)임
    # edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태.
    ex1 = [[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10],
            [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]]
    ex2 = [[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
           [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6],
            [3, 7], [4, 8], [6, 9], [9, 10]]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
