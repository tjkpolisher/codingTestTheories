import sys
input = sys.stdin.readline


def is_in_the_system(x, y, cx, cy, r):
    d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
    return d < r


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # 출발점, 도착점 좌표
    n = int(input())  # 행성계의 개수
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())  # 각 행성계의 중점과 반지름
        start = is_in_the_system(x1, y1, cx, cy, r)
        end = is_in_the_system(x2, y2, cx, cy, r)
        if (start and not end) or (not start and end):
            cnt += 1
    print(cnt)