from collections import deque
from itertools import permutations

N = int(input())
hp = list(map(int, input().split()))

hp = hp + [0] * (3 - N)
visited = [[[0 for i in range(61)] for j in range(61)] for k in range(61)]
perms = list(permutations([9, 3, 1], 3))

q = deque([[hp, 0]])
while q:
    hp, cnt = q.popleft()
    if hp == [0, 0, 0]:
        print(cnt)
        break
    for p in perms:
        new_hp = [max(hp[i] - p[i], 0) for i in range(3)]
        if not visited[new_hp[0]][new_hp[1]][new_hp[2]]:
            visited[new_hp[0]][new_hp[1]][new_hp[2]] = 1
            q.append([new_hp, cnt + 1])