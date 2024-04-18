from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

cards.sort()
for m in Ms:
    start = bisect_left(cards, m)
    end = bisect_right(cards, m)
    print(end - start, end=' ')