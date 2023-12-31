def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum(list(range(a, b+1)))
    return answer