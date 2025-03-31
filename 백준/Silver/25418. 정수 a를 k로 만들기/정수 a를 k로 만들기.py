from collections import deque

A, K = map(int, input().split())

graph = [[] for _ in range(K + 1)]
for i in range(A, K + 1):
    tmp1 = i + 1
    tmp2 = i * 2

    # 계산한 값들이 K 이하일 때만 그래프에 append
    if tmp1 <= K:
        graph[i].append(tmp1)
    if tmp2 <= K:
        graph[i].append(tmp2)

visited = [False for _ in range(K + 1)]


def bfs(start):
    # 큐 초기화 및 시작 노드(A번 노드) 방문 처리
    q = deque()
    visited[start] = True
    for node in graph[start]:
        q.append(node)
    cnt = 0  # 연산 횟수
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            visited[x] = True
            for j in graph[x]:
                if not visited[j]:
                    q.append(j)
        cnt += 1
        if visited[K]:
            return cnt


print(bfs(A))