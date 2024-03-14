N = int(input())
p = int(input())
graph = dict()
for _ in range(p):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    # v에서 u로 가는 양방향 연결을 고려해야 함(이 문제는 간선의 방향성이 없기 때문)
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

infected = set()


def dfs(node, visited):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited)


dfs(1, infected)

print(len(infected) - 1)