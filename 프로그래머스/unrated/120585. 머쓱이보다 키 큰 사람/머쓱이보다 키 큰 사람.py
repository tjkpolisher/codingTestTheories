def solution(array, height):
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer