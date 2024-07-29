import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            popped = heappop(heap)
            print(popped[1])
    else:
        heappush(heap, (-x, x))