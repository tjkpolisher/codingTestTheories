def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
    answer = sorted(answer)
    return answer