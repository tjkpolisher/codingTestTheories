import sys
input = sys.stdin.readline

n = int(input())
dict1 = {}
dict2 = {}

for _ in range(n):
    x, y = map(int, input().split())

    if x not in dict1:
        dict1[x] = [y]
    else:
        dict1[x].append(y)
    if y not in dict2:
        dict2[y] = [x]
    else:
        dict2[y].append(x)

cnt = 0
for key in dict1:
    if len(dict1[key]) >= 2:
        cnt += 1
for key in dict2:
    if len(dict2[key]) >= 2:
        cnt += 1

print(cnt)