import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cost = 0
visited = [False] * N
ans = 10 ** 9


def dfs(depth, node):
    global ans, cost
    if depth == N - 1:
        if graph[node][0]:
            cost += graph[node][0]
            if cost < ans:
                ans = cost
            cost -= graph[node][0]
        return

    for i in range(1, N):
        if not visited[i] and graph[node][i]:
            visited[i] = True
            cost += graph[node][i]
            dfs(depth + 1, i)
            visited[i] = False
            cost -= graph[node][i]


dfs(0, 0)
print(ans)