import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

cnt = 0
if n in S:
    print(cnt)
else:
    A = 0
    B = 0
    for num in S:
        if num < n:
            A = num
        elif num > n and B == 0:
            B = num
    B -= 1
    A += 1
    cnt = (n - A) * (B - n + 1) + (B - n)
    print(cnt)