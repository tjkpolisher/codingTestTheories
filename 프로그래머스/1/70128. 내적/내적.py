def solution(a, b):
    dot_product = [a[i] * b[i] for i in range(len(a))]
    return sum(dot_product)