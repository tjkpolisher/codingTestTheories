import sys
from collections import deque
input = sys.stdin.readline

P, N = map(int, input().split())
A_array = list(map(int, input().split()))

n_items = 0
A_queue = deque(sorted(A_array))
while P < 200 and A_queue:
    A = A_queue.popleft()
    P += A
    n_items += 1

print(n_items)