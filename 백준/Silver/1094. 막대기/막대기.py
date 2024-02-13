from collections import deque
X = int(input())
sticks = deque([64])
shortest = 64
while shortest >= 1:
    shortest /= 2
    sticks.append(shortest)
    if sticks[0] > X:
        sticks.popleft()

cnt = 0
ans = 0
while ans < X:
    stick = sticks.popleft()
    if ans + stick <= X:
        ans += stick
        cnt += 1
print(cnt)