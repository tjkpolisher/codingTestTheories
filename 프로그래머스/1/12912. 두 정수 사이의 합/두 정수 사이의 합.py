def solution(a, b):
    if a > b:
        a, b = b, a
    answer = b * (b + 1) // 2 - (a - 1) * a // 2
    return answer
