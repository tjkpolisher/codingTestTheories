import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 도시와 도로 정보를 담은 그래프
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(start, K):
    q = deque()
    q.append(start)
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 0
    answer = []
    while q:
        if cnt == K:
            while q:
                answer.append(q.popleft())
            return answer
        for _ in range(len(q)):
            v = q.popleft()
            if graph[v]:
                for i in graph[v]:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
            else:
                if not visited[i]:
                    visited[i] = True
        cnt += 1


answer = bfs(X, K)
if not answer:
    # 최단 거리가 K인 도시가 하나도 존재하지 않을 경우
    print(-1)
else:
    answer.sort()  # 오름차순 정렬
    for a in answer:
        print(a)