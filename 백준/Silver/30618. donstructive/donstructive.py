from collections import deque

N = int(input())
result = deque()

right = True

for i in range(N, 0, -1):
    if right:
        result.append(i)
    else:
        result.appendleft(i)
    right = not right

print(*result)