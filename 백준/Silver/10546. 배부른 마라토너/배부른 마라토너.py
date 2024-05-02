from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
runners = defaultdict(int)
for _ in range(N):
    runners[input().rstrip()] += 1

for _ in range(N - 1):
    name = input().rstrip()
    runners[name] -= 1
    if not runners[name]:
        del runners[name]

ans = list(runners.keys())
print(*ans)