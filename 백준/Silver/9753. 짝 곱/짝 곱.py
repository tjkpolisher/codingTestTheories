import sys
import bisect
input = sys.stdin.readline

MAX = 100_000 * 2
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False
primes = [i for i, v in enumerate(is_prime) if v]

products = set()
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        prod = primes[i] * primes[j]
        if prod > 200_000:
            break
        products.add(prod)
products = sorted(products)

T = int(input())
for _ in range(T):
    K = int(input())
    idx = bisect.bisect_left(products, K)
    print(products[idx])