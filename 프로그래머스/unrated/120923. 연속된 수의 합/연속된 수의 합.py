def solution(num, total):
    a1 = (total - (num - 1) * (num - 2) // 2) // num
    answer = list(range(a1, a1 + num))
    return answer