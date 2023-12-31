def solution(n):
    from math import sqrt
    root = sqrt(n)
    if int(root) != root:
        answer = -1
    else:
        answer = (root + 1) ** 2
    return answer