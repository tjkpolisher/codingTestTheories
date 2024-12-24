import sys
from math import floor
input = sys.stdin.readline

while True:
    try:
        # a, b, c, d: 연료 소비율 계수, m: 달려야 하는 거리, t: 총 연료량
        a, b, c, d, m, t = map(float, input().split())
    except ValueError:
        break

    # 이진 탐색 범위 설정
    start = 1
    end = 10 ** 9
    v = 0  # 찾고자 하는 속도

    for _ in range(100):
        mid = (start + end) / 2
        if m / mid * (a * mid ** 4 + b * mid ** 3 + c * mid ** 2 + d * mid) > t:
            end = mid
        else:
            start = mid
            v = mid

    print(f"{floor(v * 100) / 100:0.2f}")