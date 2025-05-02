import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
tmp = B

while tmp > A:
    if tmp % 10 == 1:
        tmp = (tmp - 1) // 10
        cnt += 1
    elif tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    else:
        print(-1)
        sys.exit()

if tmp == A:
    print(cnt + 1)
else:
    print(-1)