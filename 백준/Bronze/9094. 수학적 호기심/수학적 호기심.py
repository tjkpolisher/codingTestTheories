import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for b in range(2, n):
        for a in range(1, b):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1
    print(cnt)