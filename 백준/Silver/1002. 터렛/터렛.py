from math import sqrt
import sys
input = sys.stdin.readline


def circle_point(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심이 동일할 때
    if (x1, y1) == (x2, y2):
        # 반지름까지 동일해 두 원이 완전히 동일할 때
        if r1 == r2:
            return -1
        # 그렇지 않은 경우(한 원이 다른 원 내부에 있을 때)
        else:
            return 0
    else:
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # 두 원의 중심 사이의 거리
        # 두 원의 어떤 점에서도 접하지 않을 때
        if d > r1 + r2 or d < abs(r1 - r2):
            return 0
        # 두 원이 한 점에서 접할 때
        elif d == r1 + r2 or d == abs(r1 - r2):
            return 1
        # 두 원이 두 점에서 접할 때
        else:
            return 2


T = int(input().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    print(circle_point(x1, y1, r1, x2, y2, r2))