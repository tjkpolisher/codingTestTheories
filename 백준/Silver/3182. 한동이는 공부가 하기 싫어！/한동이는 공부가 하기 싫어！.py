def dfs(graph, node, visited):
    global cnt
    visited[node] = True
    v = graph[node][0]
    if not visited[v]:
        cnt += 1
        dfs(graph, v, visited)
    return cnt


N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    idx = int(input())
    graph[i].append(idx)

counters = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    global cnt
    cnt = 0
    cnt = dfs(graph, i, visited)
    counters.append((i, cnt))
counters.sort(key=lambda x: x[1], reverse=True)
print(counters[0][0])