from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
idx_list = list(map(int, input().split()))
q = deque(range(1, N + 1))

cnt = 0
for i in idx_list:
    idx = list(q).index(i)
    if idx <= len(q) // 2:  # 4-2
        while i != q[0]:
            popped = q.popleft()
            q.append(popped)
            cnt += 1
    elif idx > len(q) // 2:  # 4-3
        while i != q[0]:
            popped = q.pop()
            q.appendleft(popped)
            cnt += 1
    q.popleft()

print(cnt)