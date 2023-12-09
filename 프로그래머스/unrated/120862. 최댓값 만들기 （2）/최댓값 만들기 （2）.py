def solution(numbers):
    answer = 0
    if len(numbers)==2:
        answer = numbers[0] * numbers[1]
    else:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                temp = numbers[i] * numbers[j]
                if temp > answer:
                    answer = temp
    return answer