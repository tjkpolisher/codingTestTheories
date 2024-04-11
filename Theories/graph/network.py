# 문제 출처: 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) - 네트워크
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43162


def dfs(graph, node, visited):
    visited[node] = True
    for idx, connected in enumerate(graph[node]):
        if connected and not visited[idx]:
            dfs(graph, idx, visited)


def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer


if __name__ == "__main__":
    ex1 = [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]]
    ex2 = [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
