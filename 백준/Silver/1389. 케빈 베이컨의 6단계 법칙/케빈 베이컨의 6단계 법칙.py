from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, N):
    kb_num = [0] * (N + 1)
    cnt = 0
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque(graph[start])

    while q:
        cnt += 1
        length = len(q)
        for _ in range(length):
            v = q.popleft()
            if not visited[v]:
                visited[v] = True
                kb_num[v] = cnt
                for i in range(len(graph[v])):
                    q.append(graph[v][i])
    return sum(kb_num)


ans = 1
cnt = 10 ** 9  # 초기값
for i in range(1, N + 1):
    cnt_tmp = bfs(i, N)
    if cnt_tmp < cnt:
        ans = i
        cnt = cnt_tmp
print(ans)