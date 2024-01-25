def solution(number, limit, power):
    weight = 0
    for n in range(1, number + 1):
        divisor = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisor += 1
                if i ** 2 != n:
                    divisor += 1
            if divisor > limit:
                divisor = power
                break
        weight += divisor
    return weight