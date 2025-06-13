import sys
input = sys.stdin.readline

Q = int(input())
S = []
cnt = 0

for _ in range(Q):
    query = input().rstrip()
    if query.startswith('1'):
        x = int(query.split()[1])
        if x == 1:
            S.sort()
        elif x == 2:
            S.sort(reverse=True)
    elif query.startswith('2'):
        _, x, t = map(int, query.split())
        if x == 0:
            S.insert(0, t)
        elif x == len(S):
            S.append(t)
        else:
            S.insert(x, t)
        cnt += 1

if S:
    print(cnt)
    print(*S)