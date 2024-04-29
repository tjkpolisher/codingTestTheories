import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num1 = set(map(int, input().split()))

    M = int(input())
    num2 = list(map(int, input().split()))

    for m in num2:
        if m in num1:
            print(1)
        else:
            print(0)