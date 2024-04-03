import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(graph, node, visited):
    visited[node] = True
    next_node = graph[node][0]
    if not visited[next_node]:
        dfs(graph, next_node, visited)


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    sequence = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for i, n in enumerate(sequence):
        graph[i + 1].append(n)

    visited = [False] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1
    print(cnt)