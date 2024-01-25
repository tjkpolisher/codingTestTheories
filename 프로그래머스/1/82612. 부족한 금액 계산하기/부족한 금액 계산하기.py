def solution(price, money, count):
    total = (count * (count + 1) // 2) * price
    answer = max(total - money, 0)
    return answer