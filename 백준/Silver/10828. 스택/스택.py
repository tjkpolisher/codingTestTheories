import sys
N = int(input())
cnt = 0
stack = []
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith('push'):
        c1, c2 = cmd.split()
        stack.append(int(c2))
        cnt += 1
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            p = stack.pop()
            cnt -= 1
            print(p)
    elif cmd == 'size':
        print(cnt)
    elif cmd == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])