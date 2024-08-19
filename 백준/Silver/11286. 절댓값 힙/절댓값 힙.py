from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    integer = int(input())
    if not integer:
        if not heap:
            print(0)
        else:
            p = heappop(heap)
            print(p[1])
    else:
        heappush(heap, (abs(integer), integer))