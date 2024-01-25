def solution(a, b):
    answer = 1
    from math import gcd
    g = gcd(a, b)
    a, b = a // g, b // g
    
    p = prime_factors(b)
    if 2 in p:
        p.remove(2)
    if 5 in p:
        p.remove(5)
        
    if b == 1 or b == 2 or b == 5:
        answer = 1 
    elif len(p) > 0:
        answer = 2
    return answer

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return list(set(factors))