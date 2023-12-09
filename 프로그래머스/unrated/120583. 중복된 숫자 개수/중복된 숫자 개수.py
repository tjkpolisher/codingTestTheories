def solution(array, n):
    answer = 0
    for integer in array:
        if integer == n:
            answer += 1
    return answer