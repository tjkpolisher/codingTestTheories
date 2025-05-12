import sys
input = sys.stdin.readline

MAX_N = 123456
MAX_LIMIT = 2 * MAX_N

is_prime = [True] * (MAX_LIMIT + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i ** 2, MAX_LIMIT + 1, i):
            is_prime[j] = False

prime_count = [0] * (MAX_LIMIT + 1)
cnt = 0
for i in range(MAX_LIMIT + 1):
    if is_prime[i]:
        cnt += 1
    prime_count[i] = cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(prime_count[2 * n] - prime_count[n])