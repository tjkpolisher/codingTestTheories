import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())
    graph = [[0] * M for i in range(N)]
    for i in range(K):
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1

    larva = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                larva += 1

    print(larva)