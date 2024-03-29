from collections import deque

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = deque([(i, idx) for idx, i in enumerate(priority)])

    cnt = 0
    while True:
        if priority[0][0] == max(priority, key=lambda x: x[0])[0]:
            cnt += 1
            if priority[0][1] == M:
                print(cnt)
                break
            else:
                priority.popleft()
        else:
            priority.append(priority.popleft())