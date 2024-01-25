from math import gcd
n1, n2 = map(int, input().split())
g = gcd(n1, n2)
ans = (n1 // g) * (n2 // g) * g
print(g)
print(ans)