import sys
from collections import deque

N = int(input())
cnt = 0
q = deque()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith('push'):
        c1, c2 = cmd.split()
        q.append(int(c2))
        cnt += 1
    elif cmd == 'pop':
        if not q:
            print(-1)
        else:
            p = q.popleft()
            cnt -= 1
            print(p)
    elif cmd == 'size':
        print(cnt)
    elif cmd == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])