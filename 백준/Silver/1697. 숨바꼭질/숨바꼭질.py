from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end, visited):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        if v == end:
            return visited[end]

        for i in (v + 1, v - 1, v * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


N, K = map(int, input().split())
visited = [0] * 100001

print(bfs(N, K, visited))