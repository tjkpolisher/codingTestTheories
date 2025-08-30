import sys
from array import array
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())
heights = list(map(int, input().split()))

limit = R * C
if limit == 0 or N == 0:
    print(0)
    raise SystemExit

MAX_H = 1_000_000
cnt = array('H', [0]) * (MAX_H + 1)

visible_count = 0
for h in heights:
    if visible_count == limit:
        break
    # 각 높이별로 최대 C개까지만 집계
    if cnt[h] < C:
        cnt[h] += 1
        visible_count += 1

print(visible_count)