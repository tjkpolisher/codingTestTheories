import sys
input = sys.stdin.readline

prime = [True] * 1000001
for i in range(2, int(1000001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False

while True:
    n = int(input())
    if not n:
        break
    for i in range(3, n - 2, 2):
        if prime[i] and prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")