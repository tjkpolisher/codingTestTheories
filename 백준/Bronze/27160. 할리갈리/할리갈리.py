import sys
input = sys.stdin.readline

N = int(input())
table = {"STRAWBERRY":0, "BANANA":0,
         "LIME":0, "PLUM":0}
for _ in range(N):
    S, X = input().split()
    X = int(X)
    table[S] += X
values = table.values()
if 5 in values:
    print("YES")
else:
    print("NO")