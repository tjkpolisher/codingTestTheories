from collections import deque
N, K = map(int, input().split())
d = deque(range(1, N + 1))
josephus = []
while d:
    cnt = 1
    while cnt < K:
        i = d.popleft()
        d.append(i)
        cnt += 1
    josephus.append(d.popleft())

print("<", end='')
for i, j in enumerate(josephus):
    if i == len(josephus) - 1:
        print(f"{j}>")
    else:
        print(j, end=', ')