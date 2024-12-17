import sys
from math import trunc
sys.setrecursionlimit(10**6)

H, Y = map(int, sys.stdin.readline().split())
max_profit = 0


def profit(h, y):
    global max_profit
    if y == 0:  # 종료 조건
        max_profit = max(max_profit, h)
        return max_profit
    if y >= 5:
        profit(trunc(h * 1.35), y - 5)
    if y >= 3:
        profit(trunc(h * 1.2), y - 3)
    if y >= 1:
        profit(trunc(h * 1.05), y - 1)

    return max_profit


max_profit = profit(H, Y)
print(max_profit)