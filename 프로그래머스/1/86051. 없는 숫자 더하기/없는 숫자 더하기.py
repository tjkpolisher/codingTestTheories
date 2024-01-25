def solution(numbers):
    ztn = set(range(10))
    numbers = set(numbers)
    ans = list(ztn - numbers)
    answer = sum(ans)
    return answer