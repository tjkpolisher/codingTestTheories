import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    visited = {}

    for idx in range(k):
        command = sys.stdin.readline().split()

        if command[0] == 'I':
            number = int(command[1])
            heapq.heappush(min_heap, (number, idx))
            heapq.heappush(max_heap, (-number, idx))
            visited[idx] = True

        elif command[0] == 'D':
            if command[1] == '1':
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif command[1] == '-1':
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")
    else:
        print("EMPTY")
