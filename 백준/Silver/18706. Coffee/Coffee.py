import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C, P = map(int, input().split())
    delivery_fee = int(100 // P)  # 배달비 (100달러를 P명이서 나눔)

    coffee = {}  # 종류 및 사이즈별 커피 가격
    for i in range(C):
        N, S, M, L = input().rstrip().split()
        S, M, L = int(S), int(M), int(L)
        coffee[N] = (S, M, L)

    for i in range(P):
        X, Y, Z = input().rstrip().split()
        if Y == 'small':
            price = coffee[Z][0]
        elif Y == 'medium':
            price = coffee[Z][1]
        else:
            price = coffee[Z][2]

        result = delivery_fee + price
        if result % 5 == 1:
            print(X, result - 1)
        elif result % 5 == 4:
            print(X, result + 1)
        else:
            print(X, result)