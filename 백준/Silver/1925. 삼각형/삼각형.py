import sys
from math import acos, pi, inf
input = sys.stdin.readline

points = []
for _ in range(3):
    a, b = map(int, input().split())
    points.append((a, b))


def get_slope(a, b):
    x1, y1 = a
    x2, y2 = b
    if x2 == x1:
        return inf
    return (y2 - y1) / (x2 - x1)


def get_length(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_angle(a, b, c):
    return acos((a + b - c) / (2 * (a ** 0.5) * (b ** 0.5))) * 180 / pi


def solve(points):
    # 기울기 계산
    slopes = []
    for i in range(3):
        slopes.append(get_slope(points[i], points[(i + 1) % 3]))
    if len(set(slopes)) == 1:
        return "X"

    # 세 변의 길이 계산
    lengths = []
    for i in range(3):
        lengths.append(get_length(points[i], points[(i + 1) % 3]))
    if len(set(lengths)) == 1:
        return "JungTriangle"
    else:
        angles = []
        for i in range(3):
            angles.append(get_angle(lengths[i], lengths[(i + 1) % 3], lengths[(i + 2) % 3]))
        MAX_ANGLE = max(angles)

        if len(set(lengths)) == 2:
            if MAX_ANGLE > 90:
                return "Dunkak2Triangle"
            elif MAX_ANGLE == 90:
                return "Jikkak2Triangle"
            else:
                return "Yeahkak2Triangle"
        else:
            if MAX_ANGLE > 90:
                return "DunkakTriangle"
            elif MAX_ANGLE == 90:
                return "JikkakTriangle"
            else:
                return "YeahkakTriangle"


print(solve(points))