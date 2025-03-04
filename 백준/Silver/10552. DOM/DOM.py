import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, P = map(int, input().split())  # 사람의 수, 채널의 수, 시작 채널 번호
graph = [-1] * M

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if ~graph[b]:
        continue
    graph[b] = a

visited = [False] * M


def dfs(n):
    visited[n] = True

    if not ~graph[n]:
        return 0

    if visited[graph[n]]:
        return -1

    result = dfs(graph[n])
    if ~result:
        return result + 1
    return result


ans = dfs(P - 1)
print(ans)