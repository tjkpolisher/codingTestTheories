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