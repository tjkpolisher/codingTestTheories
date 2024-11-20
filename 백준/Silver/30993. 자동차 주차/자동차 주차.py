from math import factorial
N, A, B, C = map(int, input().split())
print(factorial(N) // (factorial(A) * factorial(B) * factorial(C)))