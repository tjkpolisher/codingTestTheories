import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cards = deque(map(int, input().split()))
M = int(input())
integers = {m: 0 for m in map(int, input().split())}

while cards:
    card = cards.popleft()
    if card in integers:
        integers[card] = 1

values = integers.values()
for v in values:
    print(v, end=' ')