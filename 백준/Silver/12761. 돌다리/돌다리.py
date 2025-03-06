from collections import deque

A, B, N, M = map(int, input().split())
cnt = 0  # 이동 횟수


def bfs(N, M):
    global cnt

    visited = [False] * 100001  # 방문 처리 리스트
    visited[N] = True  # 시작 노드는 방문 처리

    q = deque()
    q.append(N)
    d = [1, -1, A, -A, B, -B, A, B]  # 이동 가능한 경우의 수

    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for i in range(8):
                if i < 6:
                    nx = x + d[i]
                else:
                    nx = x * d[i]

                if 0 <= nx <= 100000 and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)

        cnt += 1
        if visited[M]:
            break


bfs(N, M)
print(cnt)