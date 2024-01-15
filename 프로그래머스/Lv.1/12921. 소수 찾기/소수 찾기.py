def solution(n):
    answer = 0
    for i in range(2, n + 1): # 판별할 수
        answer += is_prime(i)
    return answer

def is_prime(x):
    from math import sqrt
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1