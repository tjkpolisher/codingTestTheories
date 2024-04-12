# 알고리즘 분류: 플로이드-워셜 알고리즘
N, M = map(int, input().split())
INF = 10 ** 9
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][K] + graph[K][X]
if distance >= INF:
    print(-1)
else:
    print(distance)

# 예제
ex1 = """
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""
ex2 = """
4 2
1 3
2 4
3 4
"""
