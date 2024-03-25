from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]
for _ in range(N - 1):
    p, s = map(int, input().split())
    tree[p].append(s)
    tree[s].append(p)


def bfs(graph, start, visited):
    q = deque([start])

    while q:
        p = q.popleft()
        for i in graph[p]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = p


bfs(tree, 1, parent)
for i in parent[2:]:
    print(i)