from math import gcd, lcm

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    GCD = gcd(M, N)
    LCM = lcm(M, N)
    ans = x
    while ans <= LCM:
        if (ans - 1) % N + 1 == y:
            break
        ans += M
    if ans > LCM:
        print(-1)
    else:
        print(ans)