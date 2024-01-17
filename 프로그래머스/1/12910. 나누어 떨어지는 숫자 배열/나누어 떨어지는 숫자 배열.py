def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    answer.sort()
    if not answer:
        answer = [-1]
    return answer