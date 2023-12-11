from math import gcd
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    g = gcd(A, B)
    print(A * B // g)