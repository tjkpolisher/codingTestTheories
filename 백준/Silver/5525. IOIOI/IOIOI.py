import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
S = deque(input().rstrip())

P_N = ['I']
for _ in range(N):
    P_N.append('O')
    P_N.append('I')
P_N = ''.join(P_N)

q = deque()
cnt = 0
for _ in range(2 * N):
    q.append(S.popleft())
for _ in range(M - 2 * N):
    q.append(S.popleft())
    if ''.join(list(q)) == P_N:
        cnt += 1
    q.popleft()

print(cnt)