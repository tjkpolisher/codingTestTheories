N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]


def dfs(x, y):
    visited[x][y] = True
    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(nx, ny)


dfs(0, 0)

if visited[N - 1][N - 1]:
    print("HaruHaru")
else:
    print("Hing")