import sys
input = sys.stdin.readline

N = int(input())
raw_map = input().rstrip()

n_cycle = 0
for i in range(N - 1):
    if raw_map[i] == 'E' and raw_map[i + 1] == 'W':
        n_cycle += 1
if n_cycle == 0:
    n_cycle = N
print(n_cycle)