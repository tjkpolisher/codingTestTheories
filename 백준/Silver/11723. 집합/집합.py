import sys

M = int(input())
s = set()
for _ in range(M):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "all":
        s = set(range(1, 21))
    elif cmd == "empty":
        s = set()
    else:
        c, x = cmd.split()
        x = int(x)
        if c == "add" and x not in s:
            s.add(x)
        elif c == "remove" and x in s:
            s.remove(x)
        elif c == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)