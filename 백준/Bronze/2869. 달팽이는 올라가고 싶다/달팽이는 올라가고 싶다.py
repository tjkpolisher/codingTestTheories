import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
n, rem = divmod((V - B), (A - B))
if rem == 0:
    print(n)
else:
    print(n + 1)