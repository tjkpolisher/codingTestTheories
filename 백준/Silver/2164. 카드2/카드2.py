from collections import deque

N = int(input())
d = deque(range(1, N + 1))

while len(d) > 1:
    d.popleft()
    popped = d.popleft()
    d.append(popped)

print(d[0])