import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
serial = []
serial_num_sum = defaultdict(int)
for _ in range(N):
    s_num = input().rstrip()
    temp = 0
    serial.append(s_num)
    for c in s_num:
        if c in "0123456789":
            temp += int(c)
    serial_num_sum[s_num] = temp

serial.sort(key=lambda x: (len(x), serial_num_sum[x], x))
for s in serial:
    print(s)