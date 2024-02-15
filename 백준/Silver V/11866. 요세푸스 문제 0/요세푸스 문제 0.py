from collections import deque

N, K = map(int, input().split())
numbers = deque(range(1, N + 1))
josephus = []

while numbers:
    cnt = 1
    while cnt < K:
        n = numbers.popleft()
        numbers.append(n)
        cnt += 1
    josephus.append(numbers.popleft())

print("<", end='')
for i, j in enumerate(josephus):
    if i == len(josephus) - 1:
        print(j, end='>')
    else:
        print(j, end=', ')