import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    boxes = 1
    net_weight = 0
    for _ in range(N):
        weight = books.pop()
        if net_weight + weight > M:
            boxes += 1
            net_weight = weight
        else:
            net_weight += weight

    print(boxes)