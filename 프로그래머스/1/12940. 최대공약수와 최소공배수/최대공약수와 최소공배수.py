def solution(n, m):
    from math import gcd
    g = gcd(n, m)
    l = (n // g) * (m // g) * g
    answer = [g, l]
    return answer