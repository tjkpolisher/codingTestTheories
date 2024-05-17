import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    table = defaultdict(int)
    T = list(map(int, input().rstrip().split()))
    Ti = T[0]
    for i in range(1, Ti + 1):
        table[T[i]] += 1
    keys = list(table.keys())
    numbers = list(table.values())
    for i, n in enumerate(numbers):
        if n > (Ti / 2):
            print(keys[i])
            break
    else:
        print("SYJKGW")